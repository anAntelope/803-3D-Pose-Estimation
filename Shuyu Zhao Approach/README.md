# 803 Pose Estimation

## Better Collaboration

Know git basics [here](https://product.hubspot.com/blog/git-and-github-tutorial-for-beginners). (Or anywhere) 


## Environment

Use python 3.7 and virtual environment. Detailed instructions below.

## Command Line Installation

- `git clone https://github.com/anAntelope/803-pos-estimation.git`
    
    this downloads the files in the repository
    
- `cd 803-pos-estimation`

    change directory to the root of the repository 

- `python3 -m virtualenv venv`

    This creates a independent python environment under `venv` folder. Note make sure you're using
    python3.7. depending on your python installation and operating systems, 
    the command for python might be `python3`, `python3.7`, or `python`. `python3 --version` or `python3.7 --version` to make sure.
    
- On windows `> .\venv\Scripts\activate.bat` to source the virtual environment. On linux/mac, do `source venv/bin/activate` instead.
This overwrites `python` command and `pip` command to the virtual environment you just installed (instead of your system installations). From now on, you can
use `python` or `pip` instead of `python3`/`python3.6`/`pip3` etc.

- `pip install setuptools --upgrade` as some dependencies require newer setuptools to install

- `pip install -e .` to install dependencies for this project.

## Notice

- Every time terminal is re-opened be sure to do the activate step.
- edit `install_requires` in `setup.py` if you introduce new dependencies


## Other Environment Requirements

`tensorflow-gpu`  in our requirement needs
- 64 bit python installation
- Cuda And cudnn. Version depending on the tensorflow version we use.
On python 3.7 tensorflow 2 should require cuda 10.0 an the according cudnn.

OR some docker container with everything configured.

Either configuring manually or using docker may be not easy to the un-experienced.
 I suggest people help each other when in doubt.