from ultralytics import YOLO
def main():
    #model = YOLO('ultralytics/cfg/models/rt-detr/rtdetr-x.yaml').load('yolov8x-obb.pt')
    model = YOLO('ultralytics/cfg/models/v8/HIC-yolov8.yaml').load('yolov8x-obb.pt')
    model.train(data="obb.yaml", epochs=500, imgsz=1024, batch=4, workers=0)
if __name__ == '__main__':
    main()