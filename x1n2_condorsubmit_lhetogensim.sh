#!/bin/bash

echo "Starting job on " `date` #Date/time of start of job
echo "Running on: `uname -a`" #Condor job is running on this node
source /cvmfs/cms.cern.ch/cmsset_default.sh  ## if a tcsh script, use .csh instead of .sh
export SCRAM_ARCH=slc7_amd64_gcc700
eval `scramv1 project CMSSW CMSSW_9_4_0_patch1`
cd CMSSW_9_4_0_patch1/src
eval `scramv1 runtime -sh`
cd ${_CONDOR_SCRATCH_DIR}
ls

echo "Arguments $1 $2 $3 $4"

mkdir NanoAODcompatible_x1_n2-$2-$3-$4_split/
cd NanoAODcompatible_x1_n2-$2-$3-$4_split/
mkdir LHEROOT_output
mkdir GENSIM_output
mv ../GENSIM_x1_n2-$2-$3-$4_$1.lhe .
ls
cd ..
pwd

cmsRun x1n2_LHEROOT_cfg.py $1 $2 $3 $4
cmsRun x1n2_GENSIM_cfg.py $1 $2 $3 $4

cd NanoAODcompatible_x1_n2-$2-$3-$4_split/GENSIM_output
ls

xrdcp GENSIM_2017_x1_n2-$2-$3-$4_$1.root root://cmseos.fnal.gov//store/user/lpcrutgers/sthayil/rpvhiggsinos/gensim/leptonicfs/3lep/x1_n2-$2-$3-$4/
rm GENSIM_2017_x1_n2-$2-$3-$4_$1.root
