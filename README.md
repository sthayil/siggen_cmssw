# siggen_cmssw
Get GENSIM .root files from MadGraph .lhes

Instructions for x1_n2:
First, 
```
cmsrel CMSSW_9_4_0_patch1
cd src/
cmsenv
voms-proxy-init --valid 192:00 -voms cms
```

To run: 
```source 0807_lhetogensim_x1n2.sh mass_n1 mass_x1 mass_n2 #filestosplitlheinto```

Edit:
- L8-9 in 0807_lhetogensim_x1n2.sh (.lhe filepath, gensim file dir)
- L30 in x1n2_condorsubmit_lhetogensim.sh (gensim file dir format)
