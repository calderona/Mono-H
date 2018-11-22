**Madgraph OLD CARDS**


https://github.com/cms-sw/genproductions/tree/4e6dda7ecc882f106135d5a33c602f53bc4843a9/bin/MadGraph5_aMCatNLO/cards/production/13TeV/monoHiggs/Zp2HDM/Zprime_A0h_A0chichi

**2) Production of gridpacks** 

https://twiki.cern.ch/twiki/bin/view/CMS/QuickGuideMadGraph5aMCatNLO

 For 2017 MC production need to update the PDF to NNPDF3.1 NNLO 

On the cards just change the pdf to:

     lhapdf = pdlabel ! PDF set
     $DEFAULT_PDF_SETS = lhaid
     $DEFAULT_PDF_MEMBERS  = reweight_PDF

On a lxplus machine (not in a release area), you can do the following: 
 
    git clone git@github.com:cms-sw/genproductions.git genproductions (if you need to use mg 2.6.x then do the following:

    git clone git@github.com:cms-sw/genproductions.git genproductions -b mg26x)
    
    cd genproductions/bin/MadGraph5_aMCatNLO/

Run the code as: 

    ./gridpack_generation.sh <name of process card without _proc_card.dat> <folder containing cards relative to current location>

Examples: 
    
    ./gridpack_generation.sh Zprime_A0h_A0chichi_MZp500_MA0300 production/pre2017/13TeV/monoHiggs/Zp2HDM/Zprime_A0h_A0chichi/Zprime_A0h_A0chichi_MZp500_MA0500


**3) Producing the LHE files (interfaced with Pythia) +  RAW-SIM  → step0.py** 

**DISCLAIMER: For production better use the step 3.5)** 

All the code is under: 
https://github.com/calderona/Mono-H/tree/master/MonoH_2017


Pythia sequence under: 
https://github.com/calderona/Mono-H/blob/master/MonoH_2017/step0.py#L89

Important change the gridpacks: 
https://github.com/calderona/Mono-H/blob/master/MonoH_2017/step0.py#L122


Run the code as: 
      
    cmsRun step0.py 


**3.5) Producing the GEN-SIM  → step0_LHE.py** 

From an external LHE file. 

Just run the step0_LHE.py step. For running through crab use crab_step0.py and follow the next
steps as always. 

**4) Producing the premix + GEN-SIM  → step1.py** 

You need to change the input file to the one from previous step. 

Run the code as:
     
    cmsRun step1.py 

**5) Producing  AOD → step2.py** 

You need to change the input file to the one from previous step. 

Run the code as:
        
    cmsRun step1.py 



**Gridpacks from Alicia** 

    /afs/cern.ch/work/c/calderon/public/MonoH-2017/

    Zprime_A0h_A0chichi_MZp500_MA0300
