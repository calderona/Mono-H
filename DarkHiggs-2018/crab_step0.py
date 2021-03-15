from CRABClient.UserUtilities import config                                                                                         
config = config()   

config.section_("General")
config.General.transferLogs = True
config.General.requestName  = 'DarkHiggs_MonoHs_HsToWWTo2l2nu_mhs_160_mx_100_mZp_195_TuneCP5_13TeV_GENSIM'
config.General.workArea = 'crab_projects'

config.section_("JobType")
config.JobType.pluginName  = 'PrivateMC'
config.JobType.psetName    = 'EXO-RunIIFall18GS-03286_1_cfg.py'
#config.JobType.numCores = 1
#config.JobType.inputFiles = ['/cvmfs/cms.cern.ch/phys_generator/gridpacks/2017/13TeV/madgraph/V5_2.6.5/DarkHiggs/DarkHiggs_WW/HsToWWTo2l2nu/DarkHiggs_MonoHs_HsToWWTo2l2nu_mhs_160_mx_100_mZp_195_TuneCP5_13TeV_slc6_amd64_gcc630_CMSSW_9_3_16_tarball.tar.xz']


config.section_("Data")
config.Data.splitting       = 'EventBased'
config.Data.unitsPerJob     = 10 #200
config.Data.totalUnits     = 10 #10000
config.Data.outputDatasetTag = 'DarkHiggs_MonoHs_HsToWWTo2l2nu_mhs_160_mx_100_mZp_195_TuneCP5_13TeV_GENSIM'
config.Data.publication     = False
config.Data.outLFNDirBase = '/store/group/phys_muon/calderon/Phase2/'
config.Data.outputPrimaryDataset = 'CRAB_PrivateMC'

config.section_("Site")
config.Site.storageSite = 'T2_CH_CERN'
#config.Site.storageSite = 'T2_ES_IFCA'
#config.Site.whitelist = ['T2_ES_IFCA']
