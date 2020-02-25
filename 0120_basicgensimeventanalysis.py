from ROOT import *
from DataFormats.FWLite import Events, Handle

good=[0]
#good = [0,1,2,3,4,5,10,11,13,201]#200
inputfiles=[]
for i in good:
#    inputfile = "test2.root"
    inputfile = "RPV_Higgsino_oneproc_mn1_500_mx1_550_split/GENSIM_output/GENSIM_2017_RPV_Higgsino_oneproc_mn1_500_mx1_550_"+str(i)+".root" 
    inputfiles.append(inputfile)

# create handle outside of loop
handle1  = Handle ('vector<reco::GenJet>')
label1 = ("ak4GenJetsNoNu") #ak8GenJets
#label = ("prunedGenParticles")
handle  = Handle ('vector<reco::GenParticle>')
label = ("genParticles")

outputfile = "testplots_0225.root"
out_file = TFile(outputfile, 'recreate')

leptons = [11, 13]

hist_numleptons  = TH1F('hist_numleptons','numleptons',20,0,20)
hist_numjets     = TH1F('hist_numjets','numjets',30,0,30)
hist_leptonpt       = TH1F('hist_leptonpt','leptonpt',30,0,300)
hist_jetpt          = TH1F('hist_jetpt','jetpt',100,0,1000)
hist_eventht        = TH1F('hist_eventht','eventht',300,0,3000)
hist_eventhtonlyjets        = TH1F('hist_eventhtonlyjets','eventhtonlyjets',300,0,3000)
hist_leptoniso   = TH1F('hist_leptoniso','leptoniso_deltar',150,0,15)

count=0

for inputfile in inputfiles:
    events = Events (inputfile)
    print inputfile

    # loop over events
    cnt=0
    for event in events:

        numlep=0
        numjets=0
        visE=0
        visEonlyjets=0

        event.getByLabel(label, handle)
        genparticles = handle.product()
    
        for particle in genparticles:
            if particle.status() == 1: #if stable
                    if abs(particle.pdgId()) in leptons:
                        if particle.pt()>3:
                            numlep+=1
                            hist_leptonpt.Fill(particle.pt())

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
        hist_numjets.Fill(numjets)
        hist_eventht.Fill(visE)
        hist_eventhtonlyjets.Fill(visEonlyjets)

        cnt+=1

out_file.cd()
out_file.Write()
out_file.Close()
