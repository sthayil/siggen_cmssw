from ROOT import *
from DataFormats.FWLite import Events, Handle
import sys

#usage python 0120_~~~.py sys.argv[1]=mn1 sys.argv[2]=mx1 batch#=sys.argv[3] i_start=sys.argv[4] i_end=sys.argv[5]

inputfiles=[]
for i in range(int(sys.argv[4]),int(sys.argv[5])):
    inputfile = "root://cmsxrootd.fnal.gov//store/user/sthayil/rpvhiggsinos/gensim/n1x1_0318/GENSIM_2017_RPV_Higgsino_oneproc_mn1_"+sys.argv[1]+"_mx1_"+sys.argv[2]+"_"+str(i)+".root" 
    inputfiles.append(inputfile)

# create handle outside of loop
handle1  = Handle ('vector<reco::GenJet>')
label1 = ("ak4GenJetsNoNu") #ak8GenJets
handle  = Handle ('vector<reco::GenParticle>')
label = ("genParticles")

gStyle.SetOptStat("nemro")
outputfile = "testplots_"+sys.argv[1]+"_"+sys.argv[2]+"_"+sys.argv[3]+".root"
out_file = TFile(outputfile, 'recreate')

leptons = [11, 13]


hist_numjets     = TH1F('hist_numjets','numjets',30,0,30)
hist_jetpt          = TH1F('hist_jetpt','jetpt',100,0,1000)
hist_eventht        = TH1F('hist_eventht','eventht',300,0,3000)
hist_eventhtonlyjets        = TH1F('hist_eventhtonlyjets','eventhtonlyjets',300,0,3000)

hist_numleptons  = TH1F('hist_numleptons','numleptons',20,0,20)
hist_leptonpt       = TH1F('hist_leptonpt','leptonpt',30,0,300)

hist_leptoniso   = TH1F('hist_leptoniso','leptoniso',1500,0,15)
hist_numisoleptons1pt2  = TH1F('hist_numisoleptons1pt2','numisoleptons1pt2',20,0,20)
hist_iso1pt2leptonpt       = TH1F('hist_iso1pt2leptonpt','iso1pt2leptonpt',30,0,300)
#hist_numisoleptons0pt1  = TH1F('hist_numisoleptons0pt1','numisoleptons0pt1',20,0,20)
#hist_iso0pt1leptonpt       = TH1F('hist_iso0pt1leptonpt','iso0pt1leptonpt',30,0,300)
#hist_numisoleptons0pt2  = TH1F('hist_numisoleptons0pt2','numisoleptons0pt2',20,0,20)
#hist_iso0pt2leptonpt       = TH1F('hist_iso0pt2leptonpt','iso0pt2leptonpt',30,0,300)
#hist_numisoleptons0pt05  = TH1F('hist_numisoleptons0pt05','numisoleptons0pt05',20,0,20)
#hist_iso0pt05leptonpt       = TH1F('hist_iso0pt05leptonpt','iso0pt05leptonpt',30,0,300)

gROOT.ForceStyle()

count=0
#trig_ht=0
#trig_lepht=0
lepev=0

#ht1050lep=0
#ht450leppt20iso0p1=0
#ht450leppt20iso0p2=0
#ht450leppt20iso0p05=0

ht1050=0
ht450lep20=0
ht1050lep=0
ht450lep=0
ht450=0
ht450leppt20iso1pt2=0
    
tauev=0

for inputfile in inputfiles:
    events = Events (inputfile)
    print inputfile

    # loop over events
    cnt=0
    for event in events:

        numlep=0
        numisolep1pt2=0
#        numisolep0pt1=0
#        numisolep0pt2=0
#        numisolep0pt05=0
        numjets=0
        visE=0
        visEonlyjets=0

#        trig_ht_flag=0
#        trig_lepht_flag0=0
#        trig_lepht_flag1=0

        haslep=0
        hastau=0
        haslep20=0
#        lepiso0pt1pt20=0
#        lepiso0pt1pt20=0
#        lepiso0pt2pt20=0
        lepiso1pt2pt20=0

        event.getByLabel(label, handle)
        genparticles = handle.product()
    
        for particle in genparticles:
            if particle.status() == 1: #if stable
                if abs(particle.pdgId()) in leptons:
                    if particle.pt()>3 and abs(particle.eta())<2.5:
                        if abs(particle.pdgId())==15: hastau=1
                        haslep=1
                        numlep+=1
                        hist_leptonpt.Fill(particle.pt())

                        if particle.pt()>20:
                            #trig_lepht_flag0=1
                            haslep20=1

                        conept=0
                        isolation=0
                        pvec = TLorentzVector()
                        pvec.SetPtEtaPhiM(particle.pt(), particle.eta(), particle.phi(), particle.mass())
                        for oparticle in genparticles:
                            if oparticle.status() == 1:
                                opvec = TLorentzVector()
                                opvec.SetPtEtaPhiM(oparticle.pt(), oparticle.eta(), oparticle.phi(), oparticle.mass())
                                deltar = pvec.DeltaR(opvec)
                                if deltar < 0.3 and deltar > 0:
                                    conept+=oparticle.pt()
                        isolation = conept / particle.pt()
                        hist_leptoniso.Fill(isolation)

                        if isolation<1.2: 
                            numisolep1pt2+=1
                            hist_iso1pt2leptonpt.Fill(particle.pt())
                            if particle.pt()>20:
                                lepiso1pt2pt20=1

                        # if isolation<0.1: 
                        #     numisolep0pt1+=1
                        #     hist_iso0pt1leptonpt.Fill(particle.pt())
                        #     if particle.pt()>20:
                        #         lepiso0pt1pt20=1

                        # if isolation<0.2: 
                        #     numisolep0pt2+=1
                        #     hist_iso0pt2leptonpt.Fill(particle.pt())
                        #     if particle.pt()>20:
                        #         lepiso0pt2pt20=1

                        # if isolation<0.05: 
                        #     numisolep0pt05+=1
                        #     hist_iso0pt05leptonpt.Fill(particle.pt())
                        #     if particle.pt()>20:
                        #         lepiso0pt05pt20=1

                        visE+=(particle.pt())

        event.getByLabel(label1, handle1)
        genjets = handle1.product()
    
        for jet in genjets:
            if jet.pt()>30 and abs(jet.eta())<2.5:
                numjets+=1
                visE+=jet.pt()
                visEonlyjets+=jet.pt()
                hist_jetpt.Fill(jet.pt())

        hist_numleptons.Fill(numlep)
#        hist_numisoleptons0pt1.Fill(numisolep0pt1)
#        hist_numisoleptons0pt2.Fill(numisolep0pt2)
#        hist_numisoleptons0pt05.Fill(numisolep0pt05)
        hist_numjets.Fill(numjets)
        hist_eventht.Fill(visE)
        hist_eventhtonlyjets.Fill(visEonlyjets)

        if ( haslep==1 ): lepev+=1
        if ( hastau==1 ): tauev+=1
        if visEonlyjets>1050: ht1050+=1
        if visEonlyjets>450: ht450+=1
        if ( visEonlyjets>1050 and haslep==1 ): ht1050lep+=1
        if ( visEonlyjets>450 and haslep==1 ): ht450lep+=1
        if ( visEonlyjets>450 and haslep20==1 ): ht450lep20+=1
        if ( visEonlyjets>450 and haslep20==1 and lepiso1pt2pt20==1 ): ht450leppt20iso1pt2+=1

        cnt+=1
        count+=1

print "#Events, M_n1, M_x1                           : ", count, sys.argv[1], sys.argv[2]

print "Num events with tau: ", tauev
print "\nNum events with HT>1050: ", ht1050
print "Num events with HT>1050, lep: ", ht1050lep
print "Num events with HT>450, lep pT>20:", ht450lep20
print "Num events with HT>450, lep pT>20, lep iso <1.2:", ht450leppt20iso1pt2
print "Num events with HT>450, lep: ", ht450lep
print "Num events with HT>450: ", ht450

# print "\nPassing HT trig (1050 GeV)                    : ", trig_ht
# print "Passing LepHT trig (El/Mu 20 GeV, HT 450 GeV) : ", trig_lepht
# print "\n#Events with final state lepton               : ", lepev
# print "\nWith HT 1050 GeV and >0 leptons               : ", ht1050lep
# print "With El/Mu 20 GeV, HT 450 GeV                 : ", trig_lepht
# print "With El/Mu 20 GeV, Iso 0.1, HT 450 GeV        : ", ht450leppt20iso0p1
# print "With El/Mu 20 GeV, Iso 0.2, HT 450 GeV        : ", ht450leppt20iso0p2
# print "With El/Mu 20 GeV, Iso 0.05, HT 450 GeV       : ", ht450leppt20iso0p05

out_file.cd()
out_file.Write()
out_file.Close()
