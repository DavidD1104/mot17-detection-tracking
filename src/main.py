import os
import cv2
from src.detector import PersonDetector
from src.tracker import ObjectTracker
import time


IMG_DIR = "data/MOT17/train/MOT17-02-FRCNN/img1"

def main():
    image_files = sorted(os.listdir(IMG_DIR))

    detector = PersonDetector()
    tracker = ObjectTracker()

    prev_time = time.time()

    for img_name in image_files:
        img_path = os.path.join(IMG_DIR, img_name)
        frame = cv2.imread(img_path)

        if frame is None:
            continue

        detections = detector.detect(frame)
        tracks = tracker.update(detections)

        for track in tracks:
            x1, y1, x2, y2, track_id = map(int, track)
            cv2.rectangle(frame, (x1, y1), (x2, y2),
                          (0, 255, 0), 2)
            cv2.putText(frame, f"ID {track_id}",
                        (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.6, (0, 255, 0), 2)
            
        current_time = time.time()
        fps = 1.0 / (current_time - prev_time)
        prev_time = current_time

        cv2.putText(frame, f"FPS: {fps:.2f}",
                    (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 0, 255),
                    2)


        cv2.imshow("MOT17 - Detection + Tracking", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
