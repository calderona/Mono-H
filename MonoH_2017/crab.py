from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.transferLogs = True
config.General.requestName  = 'EXO-RunIIFall17wmLHEGS-Zp2HDM_Mzp500_MA0300_step0'
config.section_("General")
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName  = 'PrivateMC'
config.JobType.psetName    = 'step0.py'
config.JobType.numCores = 1

config.section_("Data")
config.Data.splitting       = 'EventBased'
config.Data.unitsPerJob     = 1000
config.Data.totalUnits 	    = 10000
config.Data.outputDatasetTag = 'EXO-RunIIFall17wmLHEGS-Zp2HDM_Mzp500_MA0300_step0'
config.Data.publication     = True
config.Data.outLFNDirBase = '/store/group/phys_higgs/cmshww/calderon/monoH-2017MC'
config.Data.outputDatasetTag = 'EXO-RunIIFall17wmLHEGS-Zp2HDM_Mzp500_MA0300_step0'
config.Data.outputPrimaryDataset = 'CRAB_PrivateMC'

config.section_("Site")
config.Site.storageSite = 'T2_CH_CERN'
#config.Site.storageSite = 'T2_ES_IFCA'
#config.Site.whitelist = ['T2_ES_IFCA']
