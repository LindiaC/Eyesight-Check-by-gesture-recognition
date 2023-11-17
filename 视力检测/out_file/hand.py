import cv2
import BaseDeploy as bd
model_path = 'out_file/hand.onnx'
cap = cv2.VideoCapture(0)
ret, img = cap.read()
model = bd(model_path)
result = model.inference(img)
print(result)
cap.release()
            