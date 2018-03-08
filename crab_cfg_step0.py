from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'ZprimeToA0hToA0chichihWWTollnunu_2HDM_MZp-600_MA0-300_Mchi1-1_ctau-1_13TeV-madgraph'
config.General.workArea = 'crab_projects'

config.JobType.pluginName = 'PrivateMC'
#config.JobType.generator = 'lhe'
config.JobType.psetName = 'EXO-RunIISummer15wmLHEGS-05152_1_cfg.py'
#config.JobType.inputFiles = ['Higgs_hzpzp_500GeV.lhe']

config.Data.outputPrimaryDataset = 'MinBias'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 100
NJOBS = 100
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/group/phys_higgs/cmshww/calderon/' 
#config.Data.outLFNDirBase = '/store/caf/user/calderon/' #'/store/user/dburns/' # or '/store/group/<subdir>'
config.Data.publication = False
#config.Data.publishDataName = 'Higgs_hzpzp_nohdecay_ww_1000GeV_13TeV_v2'

#config.Site.blacklist = ["T2_US_UCSD"]
config.section_('Site')
config.Site.storageSite = 'T2_CH_CERN'
