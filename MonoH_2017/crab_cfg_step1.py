from CRABClient.UserUtilities import config
config = config()

config.section_("General")
config.General.transferLogs = True
config.General.requestName = 'EXO-RunIIFall17wmLHEGS-Zprime_A0h_A0chichi_MZp1000_MA0300_step1' 
config.General.workArea = 'crab_projects'


config.section_("JobType")
config.JobType.pluginName  = 'Analysis'
config.JobType.psetName = 'step1.py'
config.JobType.maxMemoryMB = 2500


config.section_("Data")
config.Data.splitting       = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.outputDatasetTag = 'EXO-RunIIFall17wmLHEGS-Zprime_A0h_A0chichi_MZp1000_MA0300_step1'
config.Data.inputDBS = 'phys03'
config.Data.outLFNDirBase = '/store/group/phys_higgs/cmshww/calderon/monoH-2017MC' 
config.Data.publication = True
config.Data.inputDataset = '/CRAB_PrivateMC/calderon-EXO-RunIIFall17wmLHEGS-Zprime_A0h_A0chichi_MZp1000_MA0300_step0-794c1c222288ce370cc9331c69902371/USER'


config.section_("Site")
config.Site.storageSite = 'T2_CH_CERN'
