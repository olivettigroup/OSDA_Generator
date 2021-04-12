# OSDA_Generator

# Installation Instructions
- Clone this repository and navigate to it. 
- Create the conda enivornment. `conda env create -f env/environment.yml`
- Switch to the new environment. `conda activate osda_env`
- Run the setup file. `python setup.py install`
- Clone the Deep-Drug-Coder repository https://github.com/pcko1/Deep-Drug-Coder and navigate to it. 
- Switch the Deep-Drug-Coder branch to "nightly", `git checkout nightly`
- Install Deep-Drug-Coder `pip install .` 
- Add the environment to jupyter `python -m ipykernel install --name osda_env --display-name "osda_gen"`
