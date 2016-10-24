This tool evaluates the cross section for multiple datasets produced the CMS experiments.

Initialize a CMSSW environment and source crab.
Check out this repository, add the datasets to the file crabConfig.py and execute it.
For each dataset, a crab job (without any output) will be submitted, and after about an hour, the first results should come in.
Get the log for each dataset
```for i in crab_*; do crab status $i; done```
and then run extractXsecFromLog.py, which loops through all logs and extracts the cross section.
The file ana.py is cloned from https://raw.githubusercontent.com/syuvivida/generator/master/cross_section/runJob/ana.py

