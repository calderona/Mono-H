from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'Higgs_Zp2HDM_ww_MZP2500_MA0300_13TeV_AODSIM'
config.General.workArea = 'crab_projects'

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step3_25ns.py'
config.Data.inputDBS = 'phys03'
config.Data.ignoreLocality = True
config.Site.whitelist = ["T2_CH*"]
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
NJOBS = 10
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase =  '/store/group/phys_higgs/cmshww/calderon/' #'/store/user/dburns/' # or '/store/group/<subdir>'
#config.Data.publication = True
#config.Data.publishDataName = 'Higgs_hzpzp_nohdecay_ww_1000GeV_13TeV_AODSIM_v1'
#config.Data.primaryDataset = 'CRAB_UserFiles/15112015/MINIAODSIM' 
config.Data.userInputFiles =  open('Higgs_Zp2HDM_ww_MZP2500_MA0300_13TeV_RECO.txt').readlines()
config.section_('User')
config.section_('Site')

config.Site.storageSite = 'T2_CH_CERN'

