## 📌 Smart Zone-Wise Mess Detection System
## 🧠 Overview

The Smart Zone-Wise Mess Detection System is a computer vision-based project that uses YOLOv8 to detect and classify different types of waste and cleanliness states in images. The system is designed to analyze different zones and identify whether an area is clean or messy based on object detection.

This project can be used for:

Smart city cleanliness monitoring
Waste detection systems
Automated environmental monitoring
AI-based surveillance for hygiene management

## 🚀 Features
Real-time object detection using YOLOv8
Zone-wise mess detection logic
Dataset preprocessing and splitting
Model training and evaluation scripts
Prediction on images
Modular Python code structure
Support for custom datasets
## 📁 Project Structure
## Smart-Zone-Wise-Mess-Detection-System/
│
├── dataset/                 # Raw or processed dataset (images + labels)
│   ├── train/
│   ├── val/
│   └── test/
│
├── runs/                    # YOLO training outputs (ignored in git)
│
├── check_data.py           # Dataset validation script
├── class_adjustment.py     # Class mapping / label adjustments
├── evaluation.py           # Model evaluation script
├── predict.py             # Run inference on images
├── split.py               # Train/val/test split script
├── train.py               # YOLOv8 training script
│
├── yolov8n.pt             # Pretrained YOLOv8 model weights
│
├── README.md              # Project documentation
└── .gitignore             # Ignored files and folders

## 📊 Dataset

The dataset contains labeled images for different categories such as:

Clean areas
Cluttered/messy areas
Waste materials (plastic, paper, glass, etc.)
Dataset Usage:

Place your dataset inside the dataset/ folder:

dataset/
├── train/
├── val/
└── test/

Each folder should contain:

Images (.jpg, .png)
Labels (.txt YOLO format)


## ⚙️ Installation
## 1. Clone repository
git clone https://github.com/your-username/Smart-Zone-Wise-Mess-Detection-System.git
cd Smart-Zone-Wise-Mess-Detection-System
## 2. Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows
## 3. Install dependencies
pip install -r requirements.txt

If requirements.txt is missing, install manually:

pip install ultralytics opencv-python numpy matplotlib
🏋️ Training Model

Run training using YOLOv8:

python train.py
## 🔍 Running Inference

Test model on images:

python predict.py
## 📈 Evaluation

Evaluate model performance:

python evaluation.py
## 🧪 Results

The model outputs:

Bounding boxes around detected objects
Class labels (clean, clutter, waste types)
Confidence scores
Zone-wise classification result
## 🛠 Technologies Used
Python 🐍
YOLOv8 (Ultralytics)
OpenCV
NumPy
Matplotlib
## 📌 Future Improvements
Real-time webcam detection
Web dashboard (Flask / Streamlit)
Cloud deployment
Zone heatmap visualization
Mobile app integration
## 👩‍💻 Author

Sneha Das Karmakar

## GitHub: https://github.com/SnehaTHD82-alt

⭐ If you like this project

Give it a ⭐ on GitHub and feel free to contribute!


