from ultralytics import YOLO

model = YOLO(r'runs\detect\runs\mess_detection-2\weights\best.pt')

results = model.predict(
    source=r'my_raw_data\SMART ZONE-WISE MESS DETECTION.v1i.yolov8\test\images',
    save=True,
    conf=0.25,
)