import cv2
import numpy as np


# < 학습된 YOLO를 OPENCV를 사용해 직접 확인해보는 프로그램 >
# 학습된 데이터를 토대로 실시간으로 객체를 탐지해냄


# 학습시킨 weights, cfg, custom.names 파일을 불러옴
net = cv2.dnn.readNet("yolov3-custom_2000.weights", "yolov3-custom.cfg")
layer_names = net.getUnconnectedOutLayersNames()

classes = [line.strip() for line in open("custom.names").readlines()]

# Start webcam
cap = cv2.VideoCapture(1)

while True:
    ret, img = cap.read()
    height, width, _ = img.shape
    
    # Detect objects
    blob = cv2.dnn.blobFromImage(img, 1/255, (416, 416), (0, 0, 0), swapRB=True, crop=False)
    net.setInput(blob)
    outputs = net.forward(layer_names)
    
    # Find objects in the frame
    boxes, confidences, class_ids = [], [], []
    for output in outputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                # Object found
                cx, cy, w, h = (detection[0:4] * np.array([width, height, width, height])).astype('int')
                x, y = int(cx - w/2), int(cy - h/2)
                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)
    
    # Non-max suppression
    indices = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    # Check if there is at least one detection
    if len(indices) > 0:
        # Draw bounding box
        for i in indices.flatten():
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            confidence = str(round(confidences[i], 2))
            color = [int(c) for c in np.random.randint(0, 255, size=3)]
            cv2.rectangle(img, (x, y), (x+w, y+h), color, 2)
            cv2.putText(img, f"{label} {confidence}", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

    # Display the image
    cv2.imshow("Image", img)
    
    # Exit loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
