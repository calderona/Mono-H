from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'Higgs_hzpzp_nohdecay_ww_100GeV_13TeV_RECO'
config.General.workArea = 'crab_projects'

config.JobType.pluginName = 'Analysis'
#config.JobType.generator = 'lhe'
config.JobType.psetName = 'step2_25ns.py'
config.Data.inputDBS = 'phys03'
config.Data.ignoreLocality = True
config.Site.whitelist = ["T2_CH*"]
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 10
NJOBS = 1
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/group/phys_higgs/cmshww/calderon/' #'/store/user/dburns/' # or '/store/group/<subdir>'
config.Data.publication = False
#config.Data.publishDataName = 'Higgs_hzpzp_nohdecay_ww_1000GeV_13TeV_RECO_v1'
config.Data.userInputFiles = open('Higgs_hzpzp_nohdecay_ww_100GeV_13TeV.txt').readlines()

config.section_('User')
config.section_('Site')

config.Site.storageSite = 'T2_CH_CERN'
