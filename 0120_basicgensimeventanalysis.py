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

gROOT.ForceStyle()
gStyle.SetOptStat(111111)

outputfile = "testplots_"+sys.argv[1]+"_"+sys.argv[2]+"_"+sys.argv[3]+".root"
out_file = TFile(outputfile, 'recreate')

leptons = [11, 13]

hist_numjets     = TH1F('hist_numjets','numjets',30,0,30)
hist_jetpt          = TH1F('hist_jetpt','jetpt',70,0,700)
hist_eventht        = TH1F('hist_eventht','eventht',150,0,3000)
hist_eventhtonlyjets        = TH1F('hist_eventhtonlyjets','eventhtonlyjets',150,0,3000)

hist_numleptons  = TH1F('hist_numleptons','numleptons',20,0,20)
hist_nummu    = TH1F('hist_nummu','nummu',20,0,20)
hist_numel    = TH1F('hist_numel','numel',20,0,20)
hist_leptonpt = TH1F('hist_leptonpt','leptonpt',100,0,200)
hist_mupt     = TH1F('hist_mupt','mupt',100,0,200)
hist_elpt     = TH1F('hist_elpt','elpt',100,0,200)

hist_ht450lep_numleptons  = TH1F('hist_ht450lep_numleptons','ht450lep_numleptons',20,0,20)
hist_ht450lep_nummu       = TH1F('hist_ht450lep_nummu','ht450lep_nummu',20,0,20)
hist_ht450lep_numel       = TH1F('hist_ht450lep_numel','ht450lep_numel',20,0,20)
hist_ht450lep_leptonpt    = TH1F('hist_ht450lep_leptonpt','ht450lep_leptonpt',100,0,200)
hist_ht450lep_mupt        = TH1F('hist_ht450lep_mupt','ht450lep_mu pt',100,0,200)
hist_ht450lep_elpt        = TH1F('hist_ht450lep_elpt','ht450lep_el pt',100,0,200)

hist_leptoniso   = TH1F('hist_leptoniso','leptoniso',60,0,1.2)
hist_muiso   = TH1F('hist_muiso','muiso',60,0,1.2)
hist_eliso   = TH1F('hist_eliso','eliso',60,0,1.2)

hist_numisoleptons1pt2  = TH1F('hist_numisoleptons1pt2','numisoleptons1pt2',20,0,20)
hist_iso1pt2leptonpt       = TH1F('hist_iso1pt2leptonpt','iso1pt2leptonpt',100,0,200)

#hist_numisoleptons0pt1  = TH1F('hist_numisoleptons0pt1','numisoleptons0pt1',20,0,20)
#hist_iso0pt1leptonpt       = TH1F('hist_iso0pt1leptonpt','iso0pt1leptonpt',30,0,300)
#hist_numisoleptons0pt2  = TH1F('hist_numisoleptons0pt2','numisoleptons0pt2',20,0,20)
#hist_iso0pt2leptonpt       = TH1F('hist_iso0pt2leptonpt','iso0pt2leptonpt',30,0,300)
#hist_numisoleptons0pt05  = TH1F('hist_numisoleptons0pt05','numisoleptons0pt05',20,0,20)
#hist_iso0pt05leptonpt       = TH1F('hist_iso0pt05leptonpt','iso0pt05leptonpt',30,0,300)


count=0
lepev=0
elev=0
muev=0
tauev=0

#ht450leppt20iso0p1=0
#ht450leppt20iso0p2=0
#ht450leppt20iso0p05=0

ht1050=0

ht450lep20=0
ht450el20=0
ht450mu20=0

ht1050lep=0
ht1050el=0
ht1050mu=0

ht450lep=0
ht450el=0
ht450mu=0

ht450=0

ht450leppt20iso1pt2=0
ht450elpt20iso1pt2=0
ht450mupt20iso1pt2=0

for inputfile in inputfiles:
    events = Events (inputfile)
    print inputfile

    # loop over events
    cnt=0
    for event in events:

        numlep=0
        numel=0
        nummu=0
        numtau=0

        numisolep1pt2=0
        numisoel1pt2=0
        numisomu1pt2=0
        
#        numisolep0pt1=0
#        numisolep0pt2=0
#        numisolep0pt05=0

        numjets=0
        visE=0
        visEonlyjets=0

        haslep=0
        hastau=0
        hasmu=0
        hasel=0

        haslep20=0
        hasel20=0
        hasmu20=0

#        lepiso0pt1pt20=0
#        lepiso0pt2pt20=0
#        lepiso0pt05pt20=0

        lepiso1pt2pt20=0
        eliso1pt2pt20=0
        muiso1pt2pt20=0

        event.getByLabel(label1, handle1)
        genjets = handle1.product()
    
        for jet in genjets:
            if jet.pt()>30 and abs(jet.eta())<2.5:
                numjets+=1
                visE+=jet.pt()
                visEonlyjets+=jet.pt()
                hist_jetpt.Fill(jet.pt())

        event.getByLabel(label, handle)
        genparticles = handle.product()
    
        for particle in genparticles:
            if particle.status() == 1: #if stable
                if abs(particle.pdgId()) == 15: 
                    hastau=1
                    numtau+=1
                if abs(particle.pdgId()) in leptons:
                    if particle.pt()>3 and abs(particle.eta())<2.5:
                        haslep=1
                        numlep+=1
                        hist_leptonpt.Fill(particle.pt())
                        if abs(particle.pdgId()) == 11: 
                            hasel=1
                            numel+=1
                            hist_elpt.Fill(particle.pt())
                        elif abs(particle.pdgId()) == 13:
                            hasmu=1
                            nummu+=1
                            hist_mupt.Fill(particle.pt())
                            
                        if visEonlyjets>450:
                            hist_ht450lep_leptonpt.Fill(particle.pt())
                            if abs(particle.pdgId()) == 13: 
                                hist_ht450lep_mupt.Fill(particle.pt())
                            if abs(particle.pdgId()) == 11:                                 
                                hist_ht450lep_elpt.Fill(particle.pt())

                        if particle.pt()>20:
                            haslep20=1
                            print particle.statusFlags().fromHardProcess(), 
                            if abs(particle.pdgId()) == 11: 
                                hasel20=1
                            elif abs(particle.pdgId()) == 13: 
                                hasmu20=1

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
                        if abs(particle.pdgId()) == 11:
                            hist_eliso.Fill(isolation)
                        elif abs(particle.pdgId()) == 13:
                            hist_muiso.Fill(isolation)

                        if isolation<1.2: 
                            numisolep1pt2+=1
                            hist_iso1pt2leptonpt.Fill(particle.pt())
                            if abs(particle.pdgId()) == 11:
                                numisoel1pt2+=1
                            elif abs(particle.pdgId()) == 13:
                                numisomu1pt2+=1

                            if particle.pt()>20:
                                lepiso1pt2pt20=1
                                if abs(particle.pdgId()) == 11:
                                    eliso1pt2pt20=1
                                elif abs(particle.pdgId()) == 13:
                                    muiso1pt2pt20=1


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

        hist_numleptons.Fill(numlep)
        hist_numel.Fill(numel)
        hist_nummu.Fill(nummu)
#        hist_numisoleptons0pt1.Fill(numisolep0pt1)
#        hist_numisoleptons0pt2.Fill(numisolep0pt2)
#        hist_numisoleptons0pt05.Fill(numisolep0pt05)
        hist_numjets.Fill(numjets)
        hist_eventht.Fill(visE)
        hist_eventhtonlyjets.Fill(visEonlyjets)

        if ( haslep==1 ): lepev+=1
        if ( hasel==1 ): elev+=1
        if ( hasmu==1 ): muev+=1
        if ( hastau==1 ): tauev+=1
        if visEonlyjets>1050: ht1050+=1
        if visEonlyjets>450: ht450+=1

        if ( visEonlyjets>1050 and haslep==1 ): ht1050lep+=1
        if ( visEonlyjets>1050 and hasel==1 ): ht1050el+=1
        if ( visEonlyjets>1050 and hasmu==1 ): ht1050mu+=1

        if ( visEonlyjets>450 and haslep==1 ): ht450lep+=1
        if ( visEonlyjets>450 and hasel==1 ): ht450el+=1
        if ( visEonlyjets>450 and hasmu==1 ): ht450mu+=1

        if ( visEonlyjets>450 and haslep20==1 ): 
            ht450lep20+=1
            print "\nht450lep20 ", count #, event.EventAuxiliary.run(), event.EventAuxiliary.luminosityBlock(), event.EventAuxiliary.event()
        if ( visEonlyjets>450 and hasel20==1 ): ht450el20+=1
        if ( visEonlyjets>450 and hasmu20==1 ): ht450mu20+=1

        if ( visEonlyjets>450 and haslep20==1 and lepiso1pt2pt20==1 ): 
            ht450leppt20iso1pt2+=1
            print "\nht450lep20iso1pt2 ", count #, event.EventAuxiliary.run(), event.EventAuxiliary.luminosityBlock(), event.EventAuxiliary.event()
        if ( visEonlyjets>450 and hasel20==1 and eliso1pt2pt20==1 ): ht450elpt20iso1pt2+=1
        if ( visEonlyjets>450 and hasmu20==1 and muiso1pt2pt20==1 ): ht450mupt20iso1pt2+=1

        cnt+=1
        count+=1

print "\n#Events, M_n1, M_x1: ", count, sys.argv[1], sys.argv[2]

print "\nNum events with lep: ", lepev
print "Num events with tau: ", tauev
print "Num events with el: ", elev
print "Num events with mu: ", muev

print "\nNum events with HT>1050: ", ht1050
print "Num events with HT>1050, lep: ", ht1050lep
print "Num events with HT>1050, el: ", ht1050el
print "Num events with HT>1050, mu: ", ht1050mu

print "\nNum events with HT>450, lep pT>20:", ht450lep20
print "Num events with HT>450, el pT>20:", ht450el20
print "Num events with HT>450, mu pT>20:", ht450mu20

print "\nNum events with HT>450, lep pT>20, lep iso <1.2:", ht450leppt20iso1pt2
print "Num events with HT>450, el pT>20, el iso <1.2:", ht450elpt20iso1pt2
print "Num events with HT>450, mu pT>20, mu iso <1.2:", ht450mupt20iso1pt2

print "\nNum events with HT>450, lep: ", ht450lep
print "Num events with HT>450, el: ", ht450el
print "Num events with HT>450, mu: ", ht450mu

print "\nNum events with HT>450: ", ht450

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
