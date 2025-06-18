from ultralytics import YOLO
import cv2

# Load YOLOv8m model (downloads if not present)
model = YOLO("yolov8m.pt")

# Start webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Detect objects
    results = model.predict(source=frame, show=False, conf=0.5, verbose=False)

    # Draw results on frame
    annotated_frame = results[0].plot()

    # Show webcam feed
    cv2.imshow("YOLOv8 Object Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
