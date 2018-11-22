from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.transferLogs = True
config.General.requestName  = 'EXO-RunIIFall17wmLHEGS-Zprime_A0h_A0chichi_MZp1000_MA0300_step0'
config.section_("General")
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName  = 'PrivateMC'
config.JobType.psetName    = 'step0_LHE.py'
#config.JobType.numCores = 1
config.JobType.inputFiles = ['Zprime_A0h_A0chichi_MZp1000_MA0300.lhe']
config.JobType.disableAutomaticOutputCollection = False

config.section_("Data")
config.Data.splitting       = 'EventBased'
config.Data.unitsPerJob     = 10
config.Data.totalUnits 	    = 10
config.Data.outputDatasetTag = 'EXO-RunIIFall17wmLHEGS-Zprime_A0h_A0chichi_MZp1000_MA0300_step0'
config.Data.publication     = True
config.Data.outLFNDirBase = '/store/group/phys_higgs/cmshww/calderon/monoH-2017MC'
config.Data.outputPrimaryDataset = 'CRAB_PrivateMC'

config.section_("Site")
config.Site.storageSite = 'T2_CH_CERN'
#config.Site.storageSite = 'T2_ES_IFCA'
#config.Site.whitelist = ['T2_ES_IFCA']
