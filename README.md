# 2021_VRDL_HW3

## Environment

* Ubuntu 16.04.5 LTS (GNU/Linux 4.15.0-39-generic x86_64)

## Requirements

docker (recommanded):

```setup
# create the docker container, you can change the share memory size if you have more.
nvidia-docker run --name yolov4 -it -v your_coco_path/:/coco/ -v your_code_path/:/yolo --shm-size=64g nvcr.io/nvidia/pytorch:20.11-py3

# apt install required packages
apt update
apt install -y zip htop screen libgl1-mesa-glx

# pip install required packages
pip install seaborn thop

# install mish-cuda if you want to use mish activation
# https://github.com/thomasbrandon/mish-cuda
# https://github.com/JunnYu/mish-cuda
cd /
git clone https://github.com/JunnYu/mish-cuda
cd mish-cuda
python setup.py build install

# go to code folder
cd /yolo
```

Use conda to create a Python virtual environment
```setup
conda create -n open-mmlab python=3.7 -y
conda activate open-mmlab
```
Install pytorch
```setup
# CUDA 11.0
conda install pytorch==1.7.1 torchvision==0.8.2 torchaudio==0.7.2 cudatoolkit=11.0 -c pytorch
```
Install mmcv
```setup
pip install mmcv-full -f https://download.openmmlab.com/mmcv/dist/{cu_version}/{torch_version}/index.html
pip install mmcv-full -f https://download.openmmlab.com/mmcv/dist/cu110/torch1.7.1/index.html

git clone https://github.com/open-mmlab/mmcv.git
cd mmcv
pip install .
```

Install mmdetection
```setup
git clone https://github.com/open-mmlab/mmdetection.git
cd mmdetection
pip install -r requirements/build.txt
pip install -v -e .  # or "python setup.py develop"
```

To install requirements:

```setup
pip install -r requirements.txt
```

※ For running Mish models, please install https://github.com/thomasbrandon/mish-cuda

## Training

```setup
python train.py --device 0 --batch-size 8 --img 640 640 --data hw2.yaml --cfg cfg/hw2.cfg --weights 'hw2.weights' --name hw2 --epoch 60 
```

## Weight for Training Model

You can download the file here:

- [The file of weight](https://drive.google.com/file/d/1gjz7FFvbhG_0QbPQnWWrZmDXy_NqmVdD/view?usp=sharing)

## Testing

```setup
python test.py --img 640 --conf 0.0001 --batch 32 --device 0 --data hw2.yaml --cfg cfg/hw2.cfg --weights weights/best.pt --iou-thres 0.4  --task test --names data/hw2.names --save-json
```

## Google Drive link

This contains all the files that need to be used.
- [Google Drive](https://drive.google.com/drive/folders/1qCjpj7PW43pt3TibQhNta8HEryYeurDM?usp=sharing)
