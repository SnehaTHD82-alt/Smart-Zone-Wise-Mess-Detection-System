from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO('yolov8n.pt')

    model.train(
        data=r'my_raw_data\SMART ZONE-WISE MESS DETECTION.v1i.yolov8\data.yaml',
        epochs=100,        # fewer epochs — CPU training, patience will stop early anyway
        imgsz=416,        # smaller than 640 = noticeably faster on CPU, still fine for this task
        batch=8,          # smaller batch trains faster per-step on CPU
        patience=15,
        device='cpu',     # explicit, avoids any auto-detect confusion
        project='runs',
        name='mess_detection',
        workers=4,         # parallel data loading, adjust based on your CPU cores
    )