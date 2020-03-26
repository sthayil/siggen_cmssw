#!/bin/bash                                                                                                                                                                                                

for (( c=0; c<=1000; c++ ))
do  
    eosrm /store/user/sthayil/rpvhiggsinos/gensim/GENSIM_2017_RPV_Higgsino_oneproc_mn1_500_mx1_550_$c.root 
    echo $c
done

