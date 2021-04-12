# OSDA_Generator
This repository contains the code and data for Discovering Relationships between OSDAs and Zeolites through Data Mining and Generative Neural Networks. It contains a large data set of the OSDAs used to synthesize zeolite structures in different chemical environments along with the code necessary to train and utilize models cabable of generating ODSA suggestions for a given zeolite and gel chemistry system. This model utilizes the Deep-Drug-Coder model (https://github.com/pcko1/Deep-Drug-Coder) which users should look at if they want to change or understand the underlying model structure. Using the models (training or generating OSDAs) requires a GPU, however CPU only machine will be able to access the data and utilize the conformer and featurization scripts.
# Installation Instructions
- Clone this repository and navigate to it. 
- Create the conda enivornment. `conda env create -f env/environment.yml`
- Switch to the new environment. `conda activate osda_env`
- Run the setup file. `python setup.py install`
- Clone the Deep-Drug-Coder repository https://github.com/pcko1/Deep-Drug-Coder and navigate to it. 
- Switch the Deep-Drug-Coder branch to "nightly", `git checkout nightly`
- Install Deep-Drug-Coder `pip install .` 
- Add the environment to jupyter `python -m ipykernel install --name osda_env --display-name "osda_gen"`
# Data
The full data set used in the paper is available in data/Jensen_et_al_CentralScience_OSDA_Zeolite_data.xlsx. This data was automatically extracted from the scientific literature and then manually checked for accuracy. This data contains the DOI for each paper, the OSDAs utilized in the synthesis, some featurization of the OSDAs (WHIM, charge, etc), the resulting zeolite structure, some zeolite featurization taken from the IZA database (https://america.iza-structure.org/IZA-SC/ftc_table.php), and quantitative gel chemistry which specifies which elements are present within the synthesis gel. 
# Usage
The examples folder contains several example scripts for useful tasks
- Train Models- trains a new model using user-specified train/test splits.
- Generate OSDAs- generates OSDA predictions using a pre-trained model. The user specifies which zeolite structure and chemistry to target.
- Get OSDA Conformers- calculates a specified number of conformers for each OSDA molecule. Can easily be done in parallel by making copies. 
- Calculate OSDA Decriptors, Visualize OSDA Space, and Draw Molecules- demonstrates how to calculate descriptors for each molecule using RDkit and ways to visualize the models and the WHIM space of the OSDAs.
# Models 
The models folder contains pre-trained models for use in generating new OSDAs, OSDA visualization, and zeolite featurization
- OSDA_model_full- trained on the complete data set. Best choice to use for new OSDA generation.
- OSDA_model_leave_out_cha- all syntheses resulting in CHA are removed from the training set. 
- OSDA_model_leave_out_sfw- all syntheses resulting in SFW are removed from the training set. 
- zeolite_normalizer-  StandardScaler normalizer model fit on all unique zeolites. It is used to featurize each zeolite structure. (https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html)
- OSDA_normalizer- StandardScaler normalizer model fit on all unique OSDAs. It is used to normalize WHIM vectors before performing PCA analysis.
- OSDA_pca- PCA model fit on all the OSDAs. Used to reduce the dimensionality of the WHIM space for visualization. ((https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html)
# Issues
Please report any issues found by opening an issue in this repository. We will try to respond to all raised issues promptly. 
# Cite
Citation to follow soon. 
