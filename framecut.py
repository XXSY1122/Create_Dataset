import cv2
import os

# 동영상 프레임 추출 코드 


filepath = "C:\\Users\\leseu\\Downloads\\worldcon_1.mp4"    #동영상 경로
video = cv2.VideoCapture(filepath)
frame_count=int(video.get(cv2.CAP_PROP_FRAME_COUNT))
#print(frame_count)
n=0
for i in range(frame_count):
    ret, frame=video.read()
    if ret and i%13==0:
        n+=1
        image_path=f"C:\\Users\\leseu\\Downloads\\worldcon_1\\{n}.jpg"  #저장 경로
        cv2.imwrite(image_path, frame)
video.release()
