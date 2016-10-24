#!/usr/bin/env python2
from WMCore.Configuration import Configuration
import os
import subprocess

config = Configuration()

config.section_("General")
config.General.requestName   = 'requestName'
config.General.transferOutputs = True
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName  = 'Analysis'
config.JobType.psetName = os.path.dirname(os.path.abspath(__file__)) + "/ana.py"
config.JobType.pyCfgParams = []

config.section_("Data")
config.Data.inputDataset = ''
config.Data.publication = False
config.Data.inputDBS = 'global'
config.Data.outputDatasetTag = 'v0'
config.Data.outLFNDirBase = "/store/user/kiesel/13TeV/nTuples/"
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1000000

config.section_("Site")
config.Site.storageSite = 'T2_DE_RWTH'

datasets = [
    '/GJets_HT-40To100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM',
]

if __name__ == '__main__':
    from CRABAPI.RawCommand import crabCommand
    import CRABClient
    for dataset in datasets:
        config.General.requestName = dataset.split('/')[1]
        config.General.requestName = config.General.requestName[:100]
        config.Data.inputDataset = dataset
        crabCommand('submit', config = config)

