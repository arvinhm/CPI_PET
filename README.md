# CPI_PET
Deep learning lesion detection

First Install CPIPackage

"cd ~/CPIPackage"
and "pip install ."


For extarcting the feature from CT and PET based on your segmentation (in our case "Lung" and "FDG avid tumor") run the below code


"CPI --input /path/to/input --output /path/to/output"



--input: folder contains all files from all patients orgonized as below
#├── patient_1
#│   ├── ct
#│   │   ├── raw
#│   │   │   └── ai_ACRIN-NSCLC-FDG-PET-001_19600110_0.seg.dcm
#│   │   └── segmentation
#│   │       └── ai_ACRIN-NSCLC-FDG-PET-001_19600722_0.seg.dcm
#│   └── pet
#│       ├── raw
#│       │   └── ai_ACRIN-NSCLC-FDG-PET-002_19600124_0.seg.dcm
#│       └── segmentation
#│           └── ai_ACRIN-NSCLC-FDG-PET-002_19600531_0.seg.dcm

--output: folder where use to save the npy and csv extarcted features
