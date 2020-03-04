# siggen_cmssw
Get GENSIM .root files from MadGraph .lhes

First, 
```
cmsrel CMSSW_9_3_4
cd src/
cmsenv
voms-proxy-init --valid 192:00 -voms cms
```

To run: 
```source 0225_lhetogensim.sh mass_n1 mass_x1 #filestosplitlheinto```

Fix:
- L24 in 0225_lhetogensim.sh has input .lhe filepath hardcoded
- L27 in condorsubmit_lhetogensim.sh has my LPC EOS area hardcoded
