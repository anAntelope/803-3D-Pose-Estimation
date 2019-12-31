# 803 Pose Estimation

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


## Other Environment Requirements

`tensorflow-gpu`  in our requirement needs
- 64 bit python installation
- Cuda And cudnn. Version depending on the tensorflow version we use.
On python 3.7 tensorflow 2 should require cuda 10.0 an the according cudnn.
