import FWCore.ParameterSet.Config as cms

externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
    args = cms.vstring('/cvmfs/cms.cern.ch/phys_generator/gridpacks/slc6_amd64_gcc481/13TeV/madgraph/V5_2.3.0/monoHiggs/Zp2HDM/Zprime_A0h_A0chichi/v1/Zprime_A0h_A0chichi_MZp600_MA0300_tarball.tar.xz'),
    nEvents = cms.untracked.uint32(5000),
    numberOfParameters = cms.uint32(1),
    outputFile = cms.string('cmsgrid_final.lhe'),
    scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh')
)

# Link to cards:
# https://github.com/cms-sw/genproductions/tree/4e6dda7ecc882f106135d5a33c602f53bc4843a9/bin/MadGraph5_aMCatNLO/cards/production/13TeV/monoHiggs/Zp2HDM/Zprime_A0h_A0chichi/Zprime_A0h_A0chichi_MZp600_MA0300

import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *

generator = cms.EDFilter("Pythia8HadronizerFilter",
                         maxEventsToPrint = cms.untracked.int32(1),
                         pythiaPylistVerbosity = cms.untracked.int32(1),
                         filterEfficiency = cms.untracked.double(1.0),
                         pythiaHepMCVerbosity = cms.untracked.bool(False),
                         comEnergy = cms.double(13000.),
                         PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CUEP8M1SettingsBlock,
        processParameters = cms.vstring(
            'SLHA:useDecayTable = off',  # Use pythia8s own decay mode instead of decays defined in LH accord
            '25:m0 = 125.0', 
            '25:onMode = off',
            '25:onIfMatch = 24 -24',           # turn ON H->WW
            '24:mMin = 0.05',                  #  
            '24:onMode = off',                 # turn OFF all W decays
            '24:onIfAny = 11 13 15 12 14 16',  # turn ON W->lnu
            'ParticleDecays:tau0Max = 1000.1',
            'LesHouches:setLifetime = 2',
            'SLHA:useDecayTable = off', # use pythia8 decay mode instead of decays defined in LH accord
            '5000522:new',
            '5000522:m0 = 1',
            '5000522:isResonance = false',
            '5000522:onMode = off',
            '5000522:mayDecay = off',
            '18:mayDecay = on',
            '18:mWidth = 0.01',  # needs to be non-zero for Pythia to decay it
            '18:onMode = off',
            '18:addChannel = 1 1 100 5000522 1 -1',
            '18:onIfAny = 5000522 1 -1',
            '18:tau0 = 1'
            ),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CUEP8M1Settings',
                                    'processParameters'
                                    )
        )
                         )

ProductionFilterSequence = cms.Sequence(generator)


# Link to generator fragment:
# https://raw.githubusercontent.com/cms-sw/genproductions/a910901267ec5e724fec5a81c853082c89d58a16/python/ThirteenTeV/monoHiggs/pythia8_hadronizer_nomatching_HWWllnunu_cff.py
