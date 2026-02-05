from ultralytics import YOLO
import numpy as np

class PersonDetector:
    def __init__(self):
        # Cargar modelo base (ligero y rápido)
        self.model = YOLO("yolov8s.pt")

    def detect(self, frame):
        """
        Returns:
        np.array([[x1, y1, x2, y2, confidence], ...])
        """
        results = self.model(frame, verbose=False)[0]
        detections = []

        for box in results.boxes:
            cls = int(box.cls[0])
            if cls == 0:  # class 0 = person
                x1, y1, x2, y2 = box.xyxy[0].tolist()
                conf = float(box.conf[0])
                detections.append([x1, y1, x2, y2, conf])

        return np.array(detections)
