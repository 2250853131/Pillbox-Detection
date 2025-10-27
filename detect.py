from ultralytics import YOLO

#model = YOLO('runs/obb/train3/weights/best.pt')
model = YOLO('runs/obb/train-HIC-Yolov8/weights/best.pt')
results = model('detect_data', save=True)
print(results[0].obb.xywhr[:, -1] * 180 / 3.1415)