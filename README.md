# Machine-Learning-With-Python
From basics to advanced 
All programs are written in python using Spyder and Jupiter Notebooks available in Anaconda. All programs are written in Anaconda2 64 bit which uses python 2 on windows platform.
# Anaconda Installation:
Step 1:Goto anaconda downloads website, and download the required file according to your system requirements.
https://www.continuum.io/downloads
Step 2: Install Anaconda
Step 3: Open Anaconda promt
Step 4: Check the version by using the command
conda -V
Step 5: Check list of packages installed, with the command
conda list
Step 6: Update conda package, with the command
conda update conda
Step 7: Update conda packages, with the command
conda update --all
Step 8: Install git, with the command
conda install git
Till this step is enough to work with the Machine Learning programs. Further steps are required to be installed to run deep learning programs. All deep learning programs are written using theano and keras.
Step 9: Install C compiler, with the commands
conda install mingw libpython
conda install pydot-ng
Step 10: Install theano, with the command
pip install Theano
The above command install's the older version of theano.
Step 11: Install the latest bleeding edge version of Theano, by cloning it from github using the command
pip install --upgrade --no-deps git+https://github.com/Theano/Theano.git
Step 12: Install Keras library wrapper for theano,
pip install git+https://github.com/fchollet/keras.git
Step 13: To open spyder shell, type the command
spyder
Note : You can also use Anaconda navigator to open Spyder, Jupiter Notebook, i-python notebook etc.
