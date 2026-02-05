from tracking.sort import Sort
import numpy as np

class ObjectTracker:
    def __init__(self):
        self.tracker = Sort()

    def update(self, detections):
        if len(detections) == 0:
            detections = np.empty((0, 5))
        return self.tracker.update(detections)
