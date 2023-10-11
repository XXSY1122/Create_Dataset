import cv2
import numpy as np

# < YOLO를 이용해 실시간 객체 탐지해보는 코드 >
# 학습된 weights, cfg, custom.names 파일 불러옴

net = cv2.dnn.readNet("yolov3-tiny-custom_2000.weights", "yolov3-tiny-custom.cfg")
layer_names = net.getUnconnectedOutLayersNames()

classes = [line.strip() for line in open("custom.names").readlines()]  # 클래스 이름 불러옴

# 웹캠 시작
cap = cv2.VideoCapture(1)

while True:
    ret, img = cap.read()  # 웹캠에서 이미지 읽음
    height, width, _ = img.shape  # 이미지의 높이와 너비 가져옴
    
    # 객체 탐지
    blob = cv2.dnn.blobFromImage(img, 1/255, (416, 416), (0, 0, 0), swapRB=True, crop=False)  # 이미지 전처리
    net.setInput(blob)  # 전처리한 이미지 네트워크에 입력
    outputs = net.forward(layer_names)  # 네트워크를 통해 객체 탐지
    
    # 프레임에서 객체 찾기
    boxes, confidences, class_ids = [], [], []
    for output in outputs:
        for detection in output:
            scores = detection[5:]  # 클래스 점수
            class_id = np.argmax(scores)  # 가장 높은 점수의 인덱스 가져옴
            confidence = scores[class_id]  # 가장 높은 점수 가져옴
            if confidence > 0.5:  # 점수가 0.5보다 크면 객체 찾은 것으로 판단함 (제대로 안되면 이값 수정)
                # 객체의 바운딩 박스 좌표 계산
                cx, cy, w, h = (detection[0:4] * np.array([width, height, width, height])).astype('int')
                x, y = int(cx - w/2), int(cy - h/2)
                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)
    
    # 너무 겹치는 박스 제거하기 (Non-max suppression)
    # 0.5보다 낮은 값은 무시함 / 0.4 (40%) 이상 겹쳐진건 박스를 제거함
    indices = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    # 하나라도 탐지가 있으면
    if len(indices) > 0:
        # 바운딩 박스 그림
        for i in indices.flatten():
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            confidence = str(round(confidences[i], 2))
            color = [int(c) for c in np.random.randint(0, 255, size=3)] # 초록색
            cv2.rectangle(img, (x, y), (x+w, y+h), color, 2)  # 사각형 그리기
            cv2.putText(img, f"{label} {confidence}", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)  # 텍스트 쓰기 (즉, 라벨 이름)

    cv2.imshow("Image", img)
    
    # 'q' 누르면 루프 나가기 (끄는거)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
