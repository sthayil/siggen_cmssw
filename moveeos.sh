#!/bin/bash                                                                                                                                                                                                

for (( c=100; c<=161; c++ ))
do  
    xrdcp -f root://cmseos.fnal.gov//store/user/sthayil/rpvhiggsinos/gensim/1000files_GENSIM_2017_RPV_Higgsino_oneproc_mn1_400_mx1_410_$c.root root://cmseos.fnal.gov//store/user/sthayil/rpvhiggsinos/gensim/GENSIM_2017_RPV_Higgsino_oneproc_mn1_400_mx1_410_$c.root
    echo $c
done

