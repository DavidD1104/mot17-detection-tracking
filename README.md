# MOT17 – Detection & Tracking with YOLO and SORT

## Overview
This project implements a real-time multi-object tracking pipeline combining a CNN-based detector (YOLOv8) with the SORT tracking algorithm.

## Pipeline
1. Frame loading from MOT17 sequences
2. Person detection using YOLOv8 (PyTorch backend)
3. Multi-object tracking with SORT
4. Real-time visualization and FPS measurement

## Technologies
- PyTorch
- YOLOv8 (Ultralytics)
- OpenCV
- SORT
- MOT17 dataset

## Results
- Real-time performance: ~XX FPS (YOLOv8n)
- Improved ID stability with YOLOv8s
- Robust tracking under moderate occlusions

## Dataset
MOT17 dataset (not included in this repository)

## Future Work
- DeepSORT integration
- Tracking metrics (MOTA, ID switches)
- Edge deployment
