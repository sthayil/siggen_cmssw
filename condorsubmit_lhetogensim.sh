#!/bin/bash

echo "Starting job on " `date` #Date/time of start of job
echo "Running on: `uname -a`" #Condor job is running on this node
source /cvmfs/cms.cern.ch/cmsset_default.sh  ## if a tcsh script, use .csh instead of .sh
export SCRAM_ARCH=slc7_amd64_gcc700
eval `scramv1 project CMSSW CMSSW_9_3_4`
cd CMSSW_9_3_4/src
eval `scramv1 runtime -sh`
cd ${_CONDOR_SCRATCH_DIR}
ls

echo "Arguments $1 $2 $3"

mkdir RPV_Higgsino_oneproc_mn1_$2_mx1_$3_split/
cd RPV_Higgsino_oneproc_mn1_$2_mx1_$3_split/
mkdir LHEROOT_output
mkdir GENSIM_output
mv ../RPV_Higgsino_oneproc_mn1_$2_mx1_$3_$1.lhe .
ls
cd ..
pwd

cmsRun LHEROOT_cfg.py $1 $2 $3
cmsRun GENSIM_cfg.py $1 $2 $3

xrdcp GENSIM_2017_RPV_Higgsino_oneproc_mn1_$2_mx1_$3_$1.root root://cmseos.fnal.gov//store/user/sthayil/rpvhiggsinos/gensim/
#rm GENSIM_2017_RPV_Higgsino_oneproc_mn1_$1_mx1_$2_$3.root
