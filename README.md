# Mono-H

## Step 1 

cmsDriver.py Hadronizer_MgmMatchTune4C_13TeV_madgraph_pythia8_Tauola_cff.py --filein file:Higgs_hzpzp_100GeV.lhe --mc --pileup_input dbs:/MinBias_TuneA2MB_13TeV-pythia8/Fall13-POSTLS162_V1-v1/GEN-SIM --eventcontent RAWSIM --pileup 2015_25ns_Startup_PoissonOOTPU --datatier GEN-SIM-RAW --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1,Configuration/DataProcessing/Utils.addMonitoring --conditions auto:run2_mc --beamspot NominalCollision2015 --magField 38T_PostLS1 --step GEN,SIM,DIGI,L1,DIGI2RAW,HLT:GRun --no_exec -n 10 --python_filename step1_25ns.py --fileout file:step1.root


## Step 2

 step2 --filein file:step1.root --fileout file:step2.root --mc --eventcontent AODSIM --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1,Configuration/DataProcessing/Utils.addMonitoring --datatier AODSIM --conditions PHYS14_25_V1 --step RAW2DIGI,L1Reco,RECO --magField 38T_PostLS1 --python_filename ste2_new.py -n 10

