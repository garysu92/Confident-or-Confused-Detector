from ultralytics import YOLO

model = YOLO("runs/detect/train2/weights/best.pt")

model.train(data="data.yaml", epochs=10)