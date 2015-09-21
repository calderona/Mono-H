# Mono-H

## Step 1 (GEN-SIM)

cmsDriver.py pythia8_hadronizer_nomatching_HWWllnunu_cff.py --filein file:Higgs_hzpzp_10GeV.lhe --mc --pileup_input dbs:/MinBias_TuneA2MB_13TeV-pythia8/Fall13-POSTLS162_V1-v1/GEN-SIM --eventcontent RAWSIM --pileup 2015_25ns_HiLum_PoissonOOTPU --datatier GEN-SIM-RAW --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1,Configuration/DataProcessing/Utils.addMonitoring --conditions auto:run2_mc --beamspot NominalCollision2015 --magField 38T_PostLS1 --step GEN,SIM,DIGI,L1,DIGI2RAW,HLT:GRun --no_exec -n 10 --python_filename step1_25ns.py --fileout file:step1.root


## Step 2 (DIGI-RECO)

cmsDriver.py  step2 --filein file:step1.root --fileout file:step2.root --mc --eventcontent AODSIM --datatier AODSIM --conditions auto:run2_mc --step RAW2DIGI,L1Reco,RECO --magField 38T_PostLS1 --python_filename step2_25ns.py -n 10


## Step 3 (MINIAOD)

step3 --filein file:step2.root --fileout file:step3.root --mc --eventcontent MINIAODSIM --runUnscheduled --datatier MINIAODSIM --conditions PHYS14_25_V1 --step PAT --python_filename step3.py --customise Configuration/DataProcessing/Utils.addMonitoring -n 10

