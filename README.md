# Real-Time Yellow Color Detection using OpenCV

This project implements a real-time yellow object detection system using the HSV color space and contour-based object localization.

The system captures live webcam input, applies HSV thresholding to isolate yellow regions, detects contours, and draws bounding boxes around detected objects in real time.

---

## 🚀 Features

- Real-time webcam processing
- HSV-based color segmentation
- Binary masking using `cv2.inRange()`
- Contour detection using `cv2.findContours()`
- Bounding box visualization for detected objects

---

## 🛠 Technologies Used

- Python
- OpenCV
- NumPy

---

## 📦 Installation

Clone the repository:

```bash
git clone <your-repo-link>
cd opencv-real-time-yellow-detection
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

```bash
python main.py
```

Press **q** to exit the webcam window.

---

## 🧠 Technical Concepts Demonstrated

- HSV color space processing
- Color-based image segmentation
- Binary thresholding
- Contour extraction
- Real-time object localization in video streams

---

## ⚠️ Note

This implementation is configured specifically for yellow color detection.  
HSV thresholds can be modified in `utils.py` to support detection of other colors.

This project was implemented as part of hands-on OpenCV exploration and demonstrates foundational computer vision techniques.