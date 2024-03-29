from detectron2.utils.logger import setup_logger
setup_logger()

# import some common libraries
import numpy as np
import os, json, cv2

# import some common detectron2 utilities
from detectron2.config import get_cfg
from detectron2 import model_zoo
from detectron2.engine import DefaultPredictor
from detectron2.utils.visualizer import Visualizer
from detectron2.data import MetadataCatalog
from detectron2.data.datasets import register_coco_instances
from detectron2.structures import BoxMode
from detectron2.utils.visualizer import ColorMode
import pycocotools.mask as mask_util
from google.colab.patches import cv2_imshow

def plot_result(dataset_dicts, path, predictor, metadata):
    for d in dataset_dicts['images']:    
        im = cv2.imread(path + d["file_name"])
        outputs = predictor(im)  
        v = Visualizer(im[:, :, ::-1],
                       metadata=metadata, 
                       scale=0.5, 
                       instance_mode= ColorMode.IMAGE_BW   # remove the colors of unsegmented pixels. This option is only available for segmentation models
        )
        out = v.draw_instance_predictions(outputs["instances"].to("cpu"))
        cv2_imshow(out.get_image()[:, :, ::-1])

def instances_to_coco_json(instances, img_id):
    """
    Dump an "Instances" object to a COCO-format json that's used for evaluation.
    Args:
        instances (Instances):
        img_id (int): the image id
    Returns:
        list[dict]: list of json annotations in COCO format.
    """
    num_instance = len(instances)
    if num_instance == 0:
        return []

    boxes = instances.pred_boxes.tensor.numpy()
    boxes = BoxMode.convert(boxes, BoxMode.XYXY_ABS, BoxMode.XYWH_ABS)
    boxes = boxes.tolist()
    scores = instances.scores.tolist()

    has_mask = instances.has("pred_masks")
    if has_mask:
        # use RLE to encode the masks, because they are too large and takes memory
        # since this evaluator stores outputs of the entire dataset
        rles = [
            mask_util.encode(np.array(mask[:, :, None], order="F", dtype="uint8"))[0]
            for mask in instances.pred_masks
        ]
        for rle in rles:
            # "counts" is an array encoded by mask_util as a byte-stream. Python3's
            # json writer which always produces strings cannot serialize a bytestream
            # unless you decode it. Thankfully, utf-8 works out (which is also what
            # the pycocotools/_mask.pyx does).
            rle["counts"] = rle["counts"].decode("utf-8")

    has_keypoints = instances.has("pred_keypoints")
    if has_keypoints:
        keypoints = instances.pred_keypoints

    results = []
    for k in range(num_instance):
        result = {
            "image_id": img_id,
            "category_id": int(1),
            "bbox": boxes[k],
            "score": scores[k],
        }
        if has_mask:
            result["segmentation"] = rles[k]
        if has_keypoints:
            # In COCO annotations,
            # keypoints coordinates are pixel indices.
            # However our predictions are floating point coordinates.
            # Therefore we subtract 0.5 to be consistent with the annotation format.
            # This is the inverse of data loading logic in `datasets/coco.py`.
            keypoints[k][:, :2] -= 0.5
            result["keypoints"] = keypoints[k].flatten().tolist()
        results.append(result)
    return results

def write_to_result(im , img_id):
    outputs = predictor(im)
    return instances_to_coco_json(outputs["instances"].to("cpu"), img_id)

if __name__=='__main__':
    register_coco_instances("my_dataset_train", {}, "train.json", "./data/train")
    cfg = get_cfg()
    cfg.DATASETS.TRAIN = ("my_dataset_train",)
    cfg.merge_from_file(model_zoo.get_config_file("COCO-InstanceSegmentation/mask_rcnn_X_101_32x8d_FPN_3x.yaml"))
    cfg.OUTPUT_DIR =("./output")
    cfg.MODEL.WEIGHTS = os.path.join(cfg.OUTPUT_DIR, "model_final.pth")  # path to the model we just trained
    cfg.TEST.DETECTIONS_PER_IMAGE = 1000
    cfg.MODEL.ROI_HEADS.NUM_CLASSES = 1  
    cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.1   # set a custom testing threshold
    predictor = DefaultPredictor(cfg)
    
    with open("test.json") as f:
        test_dict = json.load(f)

    test_files = os.listdir('./data/test')
    metadata =  MetadataCatalog.get("my_dataset_train")
    plot_result(test_dict, './data/test/', predictor, metadata)
    
    image_dict = {
        "TCGA-A7-A13E-01Z-00-DX1.png": 1,
        "TCGA-50-5931-01Z-00-DX1.png": 2,
        "TCGA-G2-A2EK-01A-02-TSB.png": 3,
        "TCGA-AY-A8YK-01A-01-TS1.png": 4,
        "TCGA-G9-6336-01Z-00-DX1.png": 5,
        "TCGA-G9-6348-01Z-00-DX1.png": 6
    }    
    answer = []
    for i in test_files:
        im = cv2.imread(f'./data/test/{i}')
        answer.extend(write_to_result(im, image_dict[i]))
    cv2.destroyAllWindows()
    json_answer = json.dumps(answer, indent=4)
    with open("answer.json", "w") as outfile:
        outfile.write(json_answer)
