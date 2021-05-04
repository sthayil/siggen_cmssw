#!/bin/bash

#usage: source 0807...sh mn1 mx1 mn2 numparts (remember to proxyinit)
echo 'Mass point : $1 , $2, $3 ; Splitting .lhe into $4 parts'
eval 'scramv1 runtime -sh' #cmsenv

#Edit filepaths
lhefile=/uscms/home/sthayil/nobackup/rpvhiggsinos/madgraph/MG5_aMC_v2_6_7/siggen/output_x1_n2_3leptons/Events/$1-$2-$3/unweighted_events.lhe 
gensimdir=/store/user/lpcrutgers/sthayil/rpvhiggsinos/gensim/leptonicfs/3lep/x1_n2-$1-$2-$3/

if [  -d "NanoAODcompatible_x1_n2-$1-$2-$3_split" ]
then
	echo Split files already present, using them.
else
	echo Splitting LHE
	mkdir NanoAODcompatible_x1_n2-$1-$2-$3_split
	python splitLHE.py $lhefile NanoAODcompatible_x1_n2-$1-$2-$3_split/GENSIM_x1_n2-$1-$2-$3_ $4 
	echo Splitting done
fi

[ ! -d con_logs ] && mkdir con_logs
[ ! -d jdl_files ] && mkdir jdl_files

eosmkdir -p /eos/uscms$gensimdir

cp x1n2_condorsubmit_lhetogensim.jdl x1n2_condorsubmit_lhetogensim_$1-$2-$3.jdl
filesubmit=x1n2_condorsubmit_lhetogensim_$1-$2-$3.jdl
sed -i "s/0000/$1/g" $filesubmit
sed -i "s/1111/$2/g" $filesubmit
sed -i "s/2222/$3/g" $filesubmit
sed -i "s/xxx/$4/g" $filesubmit

echo Using the following submit script :
cat $filesubmit
echo Submitting jobs to condor
condor_submit $filesubmit

mv $filesubmit jdl_files
