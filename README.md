# Real-Time Object Detection using YOLOv8 🚀

This project uses **YOLOv8 (You Only Look Once)** and **OpenCV** to perform real-time object detection using your webcam.

## 🔍 Features
- Detects objects in real-time from webcam
- Displays bounding boxes and labels
- Built with **YOLOv8**, **OpenCV**, and **Ultralytics**

## 🧠 Requirements
- Python 3.x
- OpenCV
- Ultralytics

## 📦 Installation

```bash
pip install opencv-python ultralytics

▶️ Run the Code
bash
Copy
Edit
python object_detect.py
Make sure your webcam is connected.

## 📸 Output
Live feed with detected objects and labels shown on screen.

📁 File Structure
bash
Copy
Edit
YOLO_ObjectDetection/
│
├── object_detect.py           # Main detection script
├── README.md                  # This file
📌 Notes
You can change the model in the code like YOLO("yolov8s.pt") or yolov8m.pt etc.

Adjust confidence threshold for more or less strict detection.

🤖 Example Models
Download models from: https://github.com/ultralytics/ultralytics

yaml
Copy
Edit

---

After saving this as `README.md` in your project folder:

### 💻 Push it to GitHub:
```bash
git init
git add .
git commit -m "Initial commit - YOLOv8 object detection"
git branch -M main
git remote add origin https://github.com/YourUsername/ObjectDetectionYOLO.git
git push -u origin main
