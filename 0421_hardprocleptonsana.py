from ROOT import *
from DataFormats.FWLite import Events, Handle
import sys

#usage python 0421_~~~.py sys.argv[1]=mn1 sys.argv[2]=mx1 batch#=sys.argv[3] i_start=sys.argv[4] i_end=sys.argv[5]

inputfiles=[]
for i in range(int(sys.argv[4]),int(sys.argv[5])):
    inputfile = "root://cmsxrootd.fnal.gov//store/user/sthayil/rpvhiggsinos/gensim/testforhui/GENSIM_2017_NanoAODcompatible_oneproc_mn1_"+sys.argv[1]+"_mx1_"+sys.argv[2]+"_"+str(i)+".root" 
#    inputfile = "root://cmsxrootd.fnal.gov//store/user/sthayil/rpvhiggsinos/gensim/n1x1_0318/GENSIM_2017_RPV_Higgsino_oneproc_mn1_"+sys.argv[1]+"_mx1_"+sys.argv[2]+"_"+str(i)+".root" 
#    inputfile = "GENSIM_2017_NanoAODcompatible_oneproc_mn1_"+sys.argv[1]+"_mx1_"+sys.argv[2]+"_"+str(i)+".root"
    inputfiles.append(inputfile)

# create handle outside of loop
handle1  = Handle ('vector<reco::GenJet>')
label1 = ("ak4GenJetsNoNu") #ak8GenJets
handle  = Handle ('vector<reco::GenParticle>')
label = ("genParticles")

gROOT.ForceStyle()
gStyle.SetOptStat(111111)

outputfile = "testforhui_testplots_"+sys.argv[1]+"_"+sys.argv[2]+"_"+sys.argv[3]+".root"
out_file = TFile(outputfile, 'recreate')

leptons = [11, 13]

hist_numjets     = TH1F('hist_numjets','numjets',30,0,30)
hist_jetpt          = TH1F('hist_jetpt','jetpt',70,0,700)
hist_eventht        = TH1F('hist_eventht','eventht',150,0,3000)

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
hist_ht450lep_mupt        = TH1F('hist_ht450lep_mupt','ht450lep_mupt',100,0,200)
hist_ht450lep_elpt        = TH1F('hist_ht450lep_elpt','ht450lep_elpt',100,0,200)

hist_leptoniso   = TH1F('hist_leptoniso','leptoniso',60,0,1.2)
hist_muiso   = TH1F('hist_muiso','muiso',60,0,1.2)
hist_eliso   = TH1F('hist_eliso','eliso',60,0,1.2)

hist_numisoleptons1pt2  = TH1F('hist_numisoleptons1pt2','numisoleptons1pt2',20,0,20)
hist_iso1pt2leptonpt       = TH1F('hist_iso1pt2leptonpt','iso1pt2leptonpt',100,0,200)

hist_hardproclep_numjets           = TH1F('hist_hardproclep_numjets',          'hardproclep_numjets',30,0,30)
hist_hardproclep_eventht           = TH1F('hist_hardproclep_eventht',          'hardproclep_eventht',150,0,3000)
hist_hardproclep_hardprocleptonpt  = TH1F('hist_hardproclep_hardprocleptonpt', 'hardproclep_hardprocleptonpt',100,0,200)
hist_hardproclep_ht450leppt        = TH1F('hist_hardproclep_ht450leppt',       'hardproclep_ht450leppt',100,0,200)
hist_hardproclep_leptoniso         = TH1F('hist_hardproclep_leptoniso',        'hardproclep_leptoniso',60,0,1.2)
hist_hardproclep_disttonearestjet  = TH1F('hist_hardproclep_disttonearestjet', 'hardproclep_disttonearestjet',20,0,2)
hist_hardproclep_ptrel             = TH1F('hist_hardproclep_ptrel',             'hardproclep_ptrel',50,0,50)
hist_hardproclep_eta               = TH1F('hist_hardproclep_eta',              'hardproclep_eta',200,-10,10)

hist_hardprocleptau_numjets           = TH1F('hist_hardprocleptau_numjets',          'hardprocleptau_numjets',30,0,30)
hist_hardprocleptau_eventht           = TH1F('hist_hardprocleptau_eventht',          'hardprocleptau_eventht',150,0,3000)
hist_hardprocleptau_hardprocleptonpt  = TH1F('hist_hardprocleptau_hardprocleptonpt', 'hardprocleptau_hardprocleptonpt',100,0,200)
hist_hardprocleptau_ht450leppt        = TH1F('hist_hardprocleptau_ht450leppt',       'hardprocleptau_ht450leppt',100,0,200)
hist_hardprocleptau_leptoniso         = TH1F('hist_hardprocleptau_leptoniso',        'hardprocleptau_leptoniso',60,0,1.2)
hist_hardprocleptau_disttonearestjet  = TH1F('hist_hardprocleptau_disttonearestjet', 'hardprocleptau_disttonearestjet',20,0,2)
hist_hardprocleptau_ptrel             = TH1F('hist_hardprocleptau_ptrel',             'hardprocleptau_ptrel',50,0,50)
hist_hardprocleptau_eta               = TH1F('hist_hardprocleptau_eta',              'hardprocleptau_eta',200,-10,10)

count=0 #global event counter
lepev=elev=muev=0

ht1050=0
ht450lep20=ht450el20=ht450mu20=0
ht1050lep=ht1050el=ht1050mu=0
ht450lep=ht450el=ht450mu=0
ht450=0
ht450leppt20iso1pt2=ht450elpt20iso1pt2=ht450mupt20iso1pt2=0

ht1050hardlep=ht450hardlep=ht450hardlep20=ht450hardlep20iso1pt2=hardlep=0

#ISOLATION CALC --------------------------------------------------------------------------------------------------------------------------------------
def isolation(particle):       
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
    iso = conept / particle.pt()
    return iso

#NEAREST JET CALC
def nearestjet(particle):
    pvec = TLorentzVector()
    pvec.SetPtEtaPhiM(particle.pt(), particle.eta(), particle.phi(), particle.mass())
    min_deltar=1000000
    closestjet='lalala' #EXCEPTIONS      
    event.getByLabel(label1, handle1)
    genjets = handle1.product()
    for jet in genjets:
        if jet.pt()>30 and abs(jet.eta())<2.5:
            jetvec=TLorentzVector()
            jetvec.SetPtEtaPhiM(jet.pt(),jet.eta(),jet.phi(),jet.mass())
            deltar = pvec.DeltaR(jetvec)
            if deltar < min_deltar and deltar > 0:
                min_deltar = deltar
                closestjet = jet
                closestjetvec = jetvec
 
    if closestjet == 'lalala':
        print "EH", cnt, "This lepton has no jets >30 GeV within eta 2.5"
        return min_deltar, 0

    else:
        flag=0 #if particle is inside jet, subtract its 4vec from the jet's 4vec
        for i in range(closestjet.numberOfDaughters()):
            daughter = closestjet.daughter(i)
            if daughter == particle: flag=1
        if flag==1:
            closestjetvec = closestjetvec - pvec

        new_closestjetvec=closestjetvec.Vect()
        ptrel = pvec.Perp(new_closestjetvec)

        return min_deltar, ptrel

#EVENT LOOP --------------------------------------------------------------------------------------------------------------------------------------------
for inputfile in inputfiles: #for each input file
    events = Events (inputfile)
    print inputfile
    cnt=0 #internal input-file counter
    for event in events: #for each event

        numlep=numel=nummu=0
        numisolep1pt2=numisoel1pt2=numisomu1pt2=0

        numjets=visEonlyjets=0

        hashardproclep=hashardprocleptau=hashardlep=0
        hashardlep20=hashardlepiso1pt2=0
        haslep=hasmu=hasel=0
        haslep20=hasel20=hasmu20=0
        lepiso1pt2pt20=eliso1pt2pt20=muiso1pt2pt20=0

        #JET STUFF    
        event.getByLabel(label1, handle1)
        genjets = handle1.product()
        for jet in genjets:
            if jet.pt()>30 and abs(jet.eta())<2.5:
                numjets+=1
                visEonlyjets+=jet.pt() #cms definition of ht
                hist_jetpt.Fill(jet.pt())

        hist_numjets.Fill(numjets)
        hist_eventht.Fill(visEonlyjets)

        #LEPTON STUFF (NO JET)
        event.getByLabel(label, handle)
        genparticles = handle.product()
        for particle in genparticles:
            if particle.status() == 1: #if stable

                #GENERAL LEPTONS
                if abs(particle.pdgId()) in leptons:

                    #HARD PROC LEPTONS
                    #Direct el/mu
                    if ( particle.statusFlags().fromHardProcess()==1 ):
                        hashardproclep=1
                        hashardlep=1
                        hist_hardproclep_numjets.Fill(numjets)
                        hist_hardproclep_eventht.Fill(visEonlyjets)
                        if visEonlyjets>450: hist_hardproclep_ht450leppt.Fill(particle.pt())
                        if particle.pt()>20 : hashardlep20 = 1
                        hist_hardproclep_hardprocleptonpt.Fill(particle.pt())
                        hist_hardproclep_eta.Fill(particle.eta())
                        iso1=isolation(particle)
                        if iso1 < 1.2 : hashardlepiso1pt2 = 1
                        hist_hardproclep_leptoniso.Fill( iso1 )
                        min_deltar, ptrel = nearestjet(particle)
                        hist_hardproclep_disttonearestjet.Fill(min_deltar)
                        hist_hardproclep_ptrel.Fill(ptrel)
                        print count, "\t", hashardprocleptau, "\t", particle.pdgId(), "\t", visEonlyjets, "\t", particle.pt(), "\t", iso1

                    #El/mu from tau
                    if ( particle.statusFlags().isHardProcessTauDecayProduct()==1 ):
                        hashardprocleptau=1
                        hashardlep=1
                        hist_hardprocleptau_numjets.Fill(numjets)  
                        hist_hardprocleptau_eventht.Fill(visEonlyjets)
                        if visEonlyjets>450: hist_hardprocleptau_ht450leppt.Fill(particle.pt())
                        if particle.pt()>20 : hashardlep20 = 1
                        hist_hardprocleptau_hardprocleptonpt.Fill(particle.pt())
                        hist_hardprocleptau_eta.Fill(particle.eta())
                        iso1=isolation(particle)
                        if iso1 < 1.2 : hashardlepiso1pt2 = 1
                        hist_hardprocleptau_leptoniso.Fill( iso1 )
                        min_deltar, ptrel = nearestjet(particle)
                        hist_hardprocleptau_disttonearestjet.Fill(min_deltar)
                        hist_hardprocleptau_ptrel.Fill(ptrel)
                        print count, "\t", hashardprocleptau, "\t", particle.pdgId(), "\t", visEonlyjets, "\t", particle.pt(), "\t", iso1
                        
                    #GEN DETECTOR LEPTONS
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
                            if abs(particle.pdgId()) == 11:
                                hasel20=1
                            elif abs(particle.pdgId()) == 13:
                                hasmu20=1

                        iso = isolation(particle)
                        hist_leptoniso.Fill(iso)
                        if abs(particle.pdgId()) == 11:
                            hist_eliso.Fill(iso)
                        elif abs(particle.pdgId()) == 13:
                            hist_muiso.Fill(iso)

                        if iso<1.2: 
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

        hist_numleptons.Fill(numlep)
        hist_numel.Fill(numel)
        hist_nummu.Fill(nummu)

        if hashardlep == 1 : hardlep+=1
        if ( visEonlyjets>1050 and hashardlep==1 ): ht1050hardlep+=1 
        if ( visEonlyjets>450 and hashardlep==1 ): ht450hardlep+=1 
        if ( visEonlyjets>450 and hashardlep20==1 ): ht450hardlep20+=1 
        if ( visEonlyjets>450 and hashardlep20==1 and hashardlepiso1pt2==1 ): ht450hardlep20iso1pt2+=1 

        if ( haslep==1 ): lepev+=1
        if ( hasel==1 ): elev+=1
        if ( hasmu==1 ): muev+=1
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
#            print "\nht450lep20 ", count, #event.run(), event.luminosityBlock(), event.event()
        if ( visEonlyjets>450 and hasel20==1 ): ht450el20+=1
        if ( visEonlyjets>450 and hasmu20==1 ): ht450mu20+=1

        if ( visEonlyjets>450 and haslep20==1 and lepiso1pt2pt20==1 ): 
            ht450leppt20iso1pt2+=1
#            print "\nht450lep20iso1pt2 ", count, #, event.EventAuxiliary.run(), event.EventAuxiliary.luminosityBlock(), event.EventAuxiliary.event()
        if ( visEonlyjets>450 and hasel20==1 and eliso1pt2pt20==1 ): ht450elpt20iso1pt2+=1
        if ( visEonlyjets>450 and hasmu20==1 and muiso1pt2pt20==1 ): ht450mupt20iso1pt2+=1

        cnt+=1
        count+=1

print "\n#Events, M_n1, M_x1: ", count, sys.argv[1], sys.argv[2]

#print "\nNum events with lep: ", lepev
#print "Num events with el: ", elev
#print "Num events with mu: ", muev

#print "\nNum events with HT>1050: ", ht1050
#print "Num events with HT>1050, lep: ", ht1050lep
#print "Num events with HT>1050, el: ", ht1050el
#print "Num events with HT>1050, mu: ", ht1050mu

#print "Num events with HT>450, lep pT>20:", ht450lep20
#print "Num events with HT>450, el pT>20:", ht450el20
#print "Num events with HT>450, mu pT>20:", ht450mu20

#print "Num events with HT>450, lep pT>20, lep iso <1.2:", ht450leppt20iso1pt2
#print "Num events with HT>450, el pT>20, el iso <1.2:", ht450elpt20iso1pt2
#print "Num events with HT>450, mu pT>20, mu iso <1.2:", ht450mupt20iso1pt2

#print "Num events with HT>450, lep: ", ht450lep
#print "Num events with HT>450, el: ", ht450el
#print "Num events with HT>450, mu: ", ht450mu

#print "\nNum events with HT>450: ", ht450

print "\nNum events with lep: ", lepev
print "Num events with HT>1050, lep > 3: ", ht1050lep
print "Num events with HT>450, lep > 3: ", ht450lep
print "Num events with HT>450, lep pT>20:", ht450lep20
print "Num events with HT>450, lep pT>20, lep iso <1.2:", ht450leppt20iso1pt2

print "\nNum events with hard proc lep: ", hardlep
print "Num events with HT>1050, hard proc lep: ", ht1050hardlep
print "Num events with HT>450, hard proc lep: ", ht450hardlep
print "Num events with HT>450, hard lep pT>20:", ht450hardlep20
print "Num events with HT>450, hard lep pT>20, hard lep iso <1.2:", ht450hardlep20iso1pt2

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
