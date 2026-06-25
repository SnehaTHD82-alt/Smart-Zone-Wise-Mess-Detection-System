from ultralytics import YOLO

model = YOLO(r'C:\Smart Zone Wise Detection\runs\detect\runs\mess_detection-2\weights\best.pt')
metrics = model.val(data=r'my_raw_data\SMART ZONE-WISE MESS DETECTION.v1i.yolov8\data.yaml')
print(metrics.box.map)      # mAP50-95
print(metrics.box.map50)    # mAP50