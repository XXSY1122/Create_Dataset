# 파일 설명

## 2000.weight = max_batch2000
-> 이거 18%?

## 4000.weight = max_batch4000
-> 이거 28%?

----
# cfg 수정해야 하는 부분들


[YOLO] 내부 filter 값을 변경한다. [YOLO] 바로 아래에 있는 [convolutional] 부분 필터만 값에 맞게 수정한다.
- 식 : (classes + 5)*3
- ex. 클래스가 1라면 18

[YOLO] 내부 classes 값을 변경한다. 학습시킬게 1개면 1으로, 3개면 3으로
