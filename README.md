# 2021_VRDL_HW3

## Environment

* COLAB
* 

## Requirements

Use conda to create a Python virtual environment
```setup
conda create -n open-mmlab python=3.7 -y
conda activate open-mmlab
```

Check cuda -version
```setup
nvcc -V
```

Install the corresponding cuda version of pytorch
```setup
# https://pytorch.org/get-started/previous-versions/
# CUDA 11.0
conda install pytorch==1.7.1 torchvision==0.8.2 torchaudio==0.7.2 cudatoolkit=11.0 -c pytorch
```

Install mmcv
```setup
# method 1
pip install mmcv-full -f https://download.openmmlab.com/mmcv/dist/{cu_version}/{torch_version}/index.html
pip install mmcv-full -f https://download.openmmlab.com/mmcv/dist/cu110/torch1.7.1/index.html

# method 2
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

## Train image

![image](https://user-images.githubusercontent.com/68366624/146068098-aec3c713-c038-411f-bbbd-5514ffa6e666.png)
![image](https://user-images.githubusercontent.com/68366624/146067557-e2fd6973-99c3-4a6d-9220-c6877acb4317.png)


## Training

```setup
python train.py --device 0 --batch-size 8 --img 640 640 --data hw2.yaml --cfg cfg/hw2.cfg --weights 'hw2.weights' --name hw2 --epoch 60 
```

## Train result

```setup
# Look at training curves in tensorboard:
%load_ext tensorboard
%tensorboard --logdir output
```
![mask_rcnn](https://user-images.githubusercontent.com/68366624/146042822-7743d756-33a1-415d-994e-f03a270954ce.png)
![total_loss](https://user-images.githubusercontent.com/68366624/146042890-7221ff30-b50e-4a05-a153-18ea52fc3fbc.png)


## Weight for Training Model

You can download the file here:

- [The file of weight](https://drive.google.com/file/d/1gjz7FFvbhG_0QbPQnWWrZmDXy_NqmVdD/view?usp=sharing)

## Testing

```setup
python test.py --img 640 --conf 0.0001 --batch 32 --device 0 --data hw2.yaml --cfg cfg/hw2.cfg --weights weights/best.pt --iou-thres 0.4  --task test --names data/hw2.names --save-json
```

## Test result

![TCGA-50-5931-01Z-00-DX1](https://user-images.githubusercontent.com/68366624/146080144-93384a81-8725-4676-8385-b56078a81985.png)
![TCGA-A7-A13E-01Z-00-DX1](https://user-images.githubusercontent.com/68366624/146081321-2df41033-67a3-41c8-8b61-ee5428d8b62f.png)
![TCGA-AY-A8YK-01A-01-TS1](https://user-images.githubusercontent.com/68366624/146081490-37f45b3e-7c71-441b-ab8c-6e853b7e050c.png)
![TCGA-G2-A2EK-01A-02-TSB](https://user-images.githubusercontent.com/68366624/146081504-838a653f-e3a3-458e-83ae-258c336f712b.png)
![TCGA-G9-6336-01Z-00-DX1](https://user-images.githubusercontent.com/68366624/146081527-49873b12-c1e6-404b-869f-39644e7a1929.png)
![TCGA-G9-6348-01Z-00-DX1](https://user-images.githubusercontent.com/68366624/146081568-cf639621-7bfe-4bc1-853a-fc0f4044fde8.png)


## Google Drive link

This contains all the files that need to be used.
- [Google Drive](https://drive.google.com/drive/folders/1qCjpj7PW43pt3TibQhNta8HEryYeurDM?usp=sharing)
