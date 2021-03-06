import FWCore.ParameterSet.Config as cms

# Disable this so that I can supply my own LHE
# externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
#     args = cms.vstring('/cvmfs/cms.cern.ch/phys_generator/gridpacks/2017/13TeV/madgraph/V5_2.4.2/WJetsToLNu-madgraphMLM/WJetsToLNu_13TeV-madgraphMLM-pythia8_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz'),
#     nEvents = cms.untracked.uint32(5000),
#     numberOfParameters = cms.uint32(1),
#     outputFile = cms.string('cmsgrid_final.lhe'),
#     scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh')
# )

#Link to datacards:
#https://github.com/cms-sw/genproductions/tree/master/bin/MadGraph5_aMCatNLO/cards/production/2017/13TeV/WJetsToLNu/WJetsToLNu_13TeV-madgraphMLM-pythia8

import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *

generator = cms.EDFilter("Pythia8HadronizerFilter",
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(13000.),
    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CP5SettingsBlock,
        processParameters = cms.vstring(
            'JetMatching:setMad = off',
            'JetMatching:scheme = 1',
            'JetMatching:merge = on',
            'JetMatching:jetAlgorithm = 2',
            'JetMatching:etaJetMax = 5.',
            'JetMatching:coneRadius = 1.',
            'JetMatching:slowJetPower = 1',
            # 'JetMatching:qCut = 19.', #this is the actual merging scale
            'JetMatching:qCut = 59.',
            # 'JetMatching:nJetMax = 4', #number of partons in born matrix element for highest multiplicity
            'JetMatching:nJetMax = 0', #number of partons in born matrix element for highest multiplicity
            'JetMatching:nQmatch = 5', #4 corresponds to 4-flavour scheme (no matching of b-quarks), 5 for 5-flavour scheme
            'JetMatching:doShowerKt = off', #off for MLM matching, turn on for shower-kT matching

            # Add a dilepton filter for faster processing
            '6:m0 = 172.5',
            '24:mMin = 0.1',
            '23:mMin = 0.1',
            'ResonanceDecayFilter:filter = on',
            'ResonanceDecayFilter:exclusive = off', #off: require at least the specified num
            'ResonanceDecayFilter:eMuAsEquivalent = off', #on: treat electrons and muons as
            'ResonanceDecayFilter:eMuTauAsEquivalent = on', #on: treat electrons, muons , an
            'ResonanceDecayFilter:allNuAsEquivalent = on', #on: treat all three neutrino fla
            'ResonanceDecayFilter:daughters = 11,11',
            'Check:abortIfVeto = on',
        ),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CP5Settings',
                                    'processParameters',
                                    )
    )
)


