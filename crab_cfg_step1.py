from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'ZprimeToA0hToA0chichihWWTollnunu_2HDM_MZp-600_MA0-300_Mchi1-1_ctau-1_13TeV-madgraph_RECO'
config.General.workArea = 'crab_projects'

config.JobType.pluginName = 'Analysis'
#config.JobType.generator = 'lhe'
config.JobType.psetName = 'EXO-RunIISummer16DR80Premix-01695_step1_cfg.py'
#config.JobType.numCores = 4
config.Data.inputDBS = 'phys03'
#config.Data.ignoreLocality = True
#config.Site.whitelist = ["T2_CH*"]
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 10
NJOBS = 10
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/group/phys_higgs/cmshww/calderon/' #'/store/user/dburns/' # or '/store/group/<subdir>'
config.Data.publication = False
#config.Data.primaryDataset = 'Higgs_Zp2HDM_ww_MZP2500_MA0300_13TeV/15112015/MINIAODSIM'
#config.Data.publishDataName = 'Higgs_hzpzp_nohdecay_ww_1000GeV_13TeV_RECO_v1'
config.Data.userInputFiles = open('EXO-RunIISummer16DR80Premix-01695_step1_GENSIM.txt').readlines()

config.section_('User')
config.section_('Site')

config.Site.storageSite = 'T2_CH_CERN'
