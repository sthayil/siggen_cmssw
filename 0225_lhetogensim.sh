#!/bin/bash

echo 'Mass point : $1 , $2 ; Splitting .lhe (100k ev) into $3 parts'

if [$1 -eq ''] || [$2 -eq ''] || [$3 -eq '']
then
	echo 'Give input mass points; splitting'
	exit 1
fi

eval 'scramv1 runtime -sh' #cmsenv

#REMINDERS:
#need to proxyinit!!
#give mn1, mx1 values as input
#use splitLHE.py to split the lhe

if [  -d "RPV_Higgsino_oneproc_mn1_$1_mx1_$2_split" ]
then
	echo Split files already present, using them.
else
	echo Splitting LHE
	mkdir RPV_Higgsino_oneproc_mn1_$1_mx1_$2_split
	python splitLHE.py /uscms/home/sthayil/nobackup/rpvhiggsinos/madgraph/MG5_aMC_v2_6_7/siggen/events_n1_x1-$1-$2/Events/run_01/unweighted_events.lhe RPV_Higgsino_oneproc_mn1_$1_mx1_$2_split/RPV_Higgsino_oneproc_mn1_$1_mx1_$2_ $3 
	echo Splitting done
fi

#edit pythia scripts (***_cfg.py)
# fileGS="runGENSIM.py"
# fileDR1="runPREMIX_1.py"
# fileDR2="runPREMIX_2.py"
# sed -i "s/RPV_Gluino_uds_oneproc/RPV_Gluino_uds_oneproc_M$1/g" $fileGS $fileDR1 $fileDR2

echo "$1 $2"

#submit jobs to condor
# mkdir con_logs

filesubmit=condorsubmit_lhetogensim.jdl
sed -i "s/0000/$1/g" $filesubmit
sed -i "s/1111/$2/g" $filesubmit
sed -i "s/xxx/$3/g" $filesubmit

echo Using the following submit script :
cat $filesubmit
echo Submitting jobs to condor
condor_submit condorsubmit_lhetogensim.jdl

sed -i "s/_$1_$2./_0000_1111./g" $filesubmit
sed -i "s/_$1_/_0000_/g" $filesubmit
sed -i "s/_$2_/_1111_/g" $filesubmit
sed -i "s/ss) $1 $2/ss) 0000 1111/g" $filesubmit
sed -i "s/eue $3/eue xxx/g" $filesubmit
echo reverted the file back to :
cat $filesubmit

