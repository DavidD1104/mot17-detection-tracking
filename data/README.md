# Dataset
This project uses the **MOT17 (Multiple Object Tracking 2017)** dataset, a standard benchmark for multi-object tracking tasks.
Due to size constraints, the dataset is not included in this repository.

Download MOT17 from:


https://motchallenge.net/data/MOT17/


After downloading, extract the dataset into the `data/` directory.

---

## Expected directory structure

The project expects the following structure:

data/
└── MOT17/
    ├── train/
    │   ├── MOT17-02-FRCNN/
    │   ├── MOT17-04-FRCNN/
    │   └── ...
    └── test/
        ├── MOT17-01-FRCNN/
        ├── MOT17-03-FRCNN/
        └── ...
