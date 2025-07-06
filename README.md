# Helmet Detection System

📌 Overview
This project is designed to detect whether two-wheeled vehicle riders are wearing helmets or not, using the YOLOv8 object detection model. A Flask-based web interface is provided to allow users to upload images or videos and automatically view detection results.

🛠️ Background
Road safety is a significant concern, especially for two-wheeled vehicle users. Helmets are a critical safety measure that significantly reduce the risk of head injuries during accidents. However, manual enforcement of helmet usage is often inconsistent and labor-intensive.
This project leverages Computer Vision to automate helmet detection, helping improve safety compliance and reduce the workload on traffic enforcement officers.

🎯 Objectives
🔍 To develop an automated object detection system focused on identifying helmet usage among motorcyclists.
🧪 To implement a real-time detection system for both image and video inputs.

🌟 Benefits
✅ Real-time detection of helmet usage
✅ Two main labels: helmet and no-helmet
✅ Visualization with bounding boxes on detected objects
✅ Counts and categorization of helmet vs. no-helmet detections

📊 Dataset
Source: Custom-labeled dataset created using Roboflow
Original Classes:
1. helmet
2. no-helmet
3. driver
4. bicyclist

However, this project focuses solely on two labels: helmet and no-helmet, using filtering during training and inference.
🔗 Dataset Link (Roboflow)
📈 Model Accuracy
* mAP@0.5: ~90%
* Precision: ~91%
* Recall: ~80%

⚙️ Input & Output Support
✅ Input Formats:
Images: .jpg, .jpeg, .png
Videos: .mp4, .avi, .mov

📸 Output:
Annotated images/videos with bounding boxes and class labels
Summary count of helmet and no-helmet detections

💻 Technologies Used
1. Python 3.x
2. YOLOv8 by Ultralytics
3. Flask
4. OpenCV
5. HTML/CSS (for web interface)
