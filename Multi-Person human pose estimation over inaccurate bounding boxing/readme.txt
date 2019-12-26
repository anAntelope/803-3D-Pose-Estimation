This code is tested under Ubuntu 16.04, CUDA 9.0, cuDNN 7.1 environment with two NVIDIA Tesla K80 GPUs.
Python 3.6.5 version with Anaconda 3 is used for development.

2D HPE: 

Root

The ${POSE_ROOT} is described as below.

${POSE_ROOT}
|-- pose_nms_test
|-- pose_nms

Just run:- python pose_nms.py  and python pose_nms_test 

Output of these two files are already dumped into models and data folders.

3D HPE:

This code is the backend implementation of 3D HPE. After obtaining 2D points, annotations are obtained on original dataset. Then, it is used by the network for being lifted up to obtain 3D pose estimations.  

Dependencies:

    PyTorch
    CUDA
    cuDNN
    Anaconda
    COCO API



Root

The ${POSE_ROOT} is described as below.

${POSE_ROOT}
|-- data
|-- common
|-- main
`-- output

    data contains data loading codes and soft links to images and annotations directories.
    common contains kernel codes for 3d multi-person pose estimation system.
    main contains high-level codes for training or testing the network.
    output contains log, trained models, visualized outputs, and test result.

Download Human3.6M parsed data : https://drive.google.com/drive/folders/1kgVH-GugrLoc9XyvP6nRoaFpw3TmM5xK?usp=sharing
Download MPII parsed data : http://human-pose.mpi-inf.mpg.de/  and https://drive.google.com/drive/folders/1MmQ2FRP0coxHGk0Ntj0JOGv9OxSNuCfK?usp=sharing

Creating output folder as soft link form is recommended instead of folder form because it would take large storage capacity.
${POSE_ROOT}
|-- output
|-- |-- log
|-- |-- model_dump
|-- |-- result
`-- |-- vis

	log folder contains training log file.
	model_dump folder contains saved checkpoints for each epoch.
	result folder contains final estimation files generated in the testing stage.
	vis folder contains visualized results.

Train:- 

In the main folder, run :- python train.py --gpu 0-1

Test

Place trained model at the output/model_dump/.

In the main folder, run :- python test.py --gpu 0-1 --test_epoch 100









