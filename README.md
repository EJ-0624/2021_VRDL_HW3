# 2021_VRDL_HW3

## Environment

* COLAB
* torch 1.10.0
* cuda 11.1

## Requirements

Install mmcv
```setup
# method 1
# pip install mmcv-full -f https://download.openmmlab.com/mmcv/dist/{cu_version}/{torch_version}/index.html
# pip install mmcv-full -f https://download.openmmlab.com/mmcv/dist/cu111/torch1.10/index.html

# method 2
git clone https://github.com/open-mmlab/mmcv.git
cd mmcv
pip install .
```

Install detectron2
```setup
# See https://detectron2.readthedocs.io/tutorials/install.html for instructions
# pip install detectron2 -f https://dl.fbaipublicfiles.com/detectron2/wheels/$CUDA_VERSION/torch$TORCH_VERSION/index.html
pip install detectron2 -f https://dl.fbaipublicfiles.com/detectron2/wheels/cu111/torch1.10/index.html
```

Install pyyaml:

```setup
pip install pyyaml==5.1
```

## Train image

![image](https://user-images.githubusercontent.com/68366624/146068098-aec3c713-c038-411f-bbbd-5514ffa6e666.png)
![image](https://user-images.githubusercontent.com/68366624/146067557-e2fd6973-99c3-4a6d-9220-c6877acb4317.png)

## Use Zen lite for image pre-processing

According to the URL
https://www.zeiss.com/microscopy/int/products/microscope-software/zen-lite.html.
register and download zen lite.


Adjust the contrast of the image to make the nucleus more visible.

![image](https://user-images.githubusercontent.com/68366624/146250908-98e82830-6c64-4ac4-bd39-8d96d50a126f.png)
![image](https://user-images.githubusercontent.com/68366624/146250883-77bf928c-60c6-4e51-b360-86fa9de11036.png)


## Get coco format

use hw3.py to get coco format and create train.json.

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

- [The file of weight](https://drive.google.com/file/d/1-0Z5-KVMfY_B-9U-PoXQQsq-_4yO5SPE/view?usp=sharing)

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
- [Google Drive](https://drive.google.com/drive/folders/1tF9ebUI0Ck86uDttJZ0s8vLNrNe6G3TZ?usp=sharing)

## 防止colab斷線
ctrl+shift+i

在console最底下輸入

```setup
function ClickConnect(){
  console.log("Working"); 
  document
    .querySelector("#top-toolbar > colab-connect-button")
    .shadowRoot
    .querySelector("#connect")
    .click()
}
 
var id=setInterval(ClickConnect,5*60000) ##每五分鐘按一次鍵
```
