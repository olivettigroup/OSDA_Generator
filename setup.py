from setuptools import setup

setup(
    name="osda_gen",
    version="1.0",
    description="Recurrent Neural Network to generate OSDAs",
    url="https://github.com/olivettigroup/OSDA_Generator",
    author="Zach Jensen",
    author_email="zjensen@mit.edu",
    license="MIT",
    install_requires=[
        "numpy          == 1.16.5",
        "h5py           == 2.9.0",
        "tensorflow-gpu == 2.0.0",
        "tqdm           == 4.35.0",
        "scikit-learn   == 0.21.3",
        "scipy          == 1.3.1",
        "ipykernel      == 5.1.1",
        "ipython",
        "matplotlib     == 3.1.1",
        "pandas         == 0.25.1",
	    "molsets        == 0.2"
    ],
    zip_safe=False,
)