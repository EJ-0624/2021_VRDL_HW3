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
python train.py
```

## Train result

```setup
# Look at training curves in tensorboard:
%load_ext tensorboard
%tensorboard --logdir output
```
![mask_rcnn](https://user-images.githubusercontent.com/68366624/146246919-1c0b5b7f-8d99-4258-a5ac-72888ba41b6e.png)
![total_loss](https://user-images.githubusercontent.com/68366624/146246975-267e6a5b-0d32-477f-9ede-2b1a22ff1c6c.png)

## Weight for Training Model

You can download the file here:

- [The file of weight](https://drive.google.com/file/d/1gjz7FFvbhG_0QbPQnWWrZmDXy_NqmVdD/view?usp=sharing)

## Testing

```setup
python inference.py
```

## Test result

![TCGA-50-5931-01Z-00-DX1](https://user-images.githubusercontent.com/68366624/146246434-3ed48a7d-bcd9-4348-b279-62fb07833e54.png)
![TCGA-A7-A13E-01Z-00-DX1](https://user-images.githubusercontent.com/68366624/146246470-266837aa-e19d-4e4b-afeb-b1dce6e723cf.png)
![TCGA-AY-A8YK-01A-01-TS1](https://user-images.githubusercontent.com/68366624/146246499-4740df46-676d-48b2-97e6-be9c3b7ef334.png)
![TCGA-G2-A2EK-01A-02-TSB](https://user-images.githubusercontent.com/68366624/146246551-cd75016e-322e-45c3-9e1d-00f11fc4fe29.png)
![TCGA-G9-6336-01Z-00-DX1](https://user-images.githubusercontent.com/68366624/146246576-009de500-4a60-497c-b44c-91228ed50d9b.png)
![TCGA-G9-6348-01Z-00-DX1](https://user-images.githubusercontent.com/68366624/146246596-fd6db5d7-b5bb-46e3-9e2c-d185f8b2c386.png)

## Google Drive link

This contains all the files that need to be used.
- [Google Drive](https://drive.google.com/drive/folders/1qCjpj7PW43pt3TibQhNta8HEryYeurDM?usp=sharing)
