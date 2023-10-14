# YOLO 학습 가이드

학습시 일부 변경해야할 파일들에 대하여 간략하게 설명함.



----
# .cfg

### [YOLO] 내부 filter 값을 변경
- [YOLO] 바로 아래에 있는 [convolutional] 부분 필터만 값에 맞게 수정한다.
- 식 : (classes + 5)*3 <br>
ex. 클래스가 1라면 18 / 클래스가 2라면 21

### [YOLO] 내부 classes 값을 변경
- 학습시킬게 1개면 1으로, 3개면 3으로

### Max_batches 값을 변경
ex. 2000~50000 임의조정

---
# detector.data

- 클래스 수에 따라 클래스 값 변경
- 각 경로 변경

<< 예시 >>
```
classes=2
train=/content/gdrive/MyDrive/custom_data/train.txt
valid=/content/gdrive/MyDrive/custom_data/test.txt
names=/content/gdrive/MyDrive/custom_data/custom.names
backup=/content/gdrive/MyDrive/custom_data/backup
```

---
# custom.names

- 클래스명 기입

<< 예시 >>
```
Melona
ChickenLeg
```

---
# 기타메모...

- 2000_weight.cfg = max_batch2000
-> 이거 18% 정도 인식

- 4000_weight.cfg = max_batch4000
-> 이거 28% 정도 인식
