import sys

sys.path.append('D:/yolov8_obb')

from ultralytics.data.converter import convert_dota_to_yolo_obb

convert_dota_to_yolo_obb('D:/yolov8_obb/data')
