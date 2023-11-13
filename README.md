# 💻 프로그램 소개 & 사용 방법

## 이미지 크롤링 용도
- crawled > crawled.py : 구글 이미지 크롤링 프로그램 (최소 200개이상의 이미지 수집)
- crawled > chromedriver.exe : win64 version / 크롤링을 위해 사용


## 데이터셋 구축용도
- framecut.py : 영상을 프레임 단위로 잘라 저장하는 프로그램
- format_to_PNG.py : 다양한 파일 형식을 PNG 파일로 모두 변경하는 프로그램
- Augmentation_for_keras : keras를 사용하여 이미지 재구성 생성하는 프로그램 (일반x5배)
- create_test_train_txt_file.py : train.txt와 test.txt 파일을 생성하는 프로그램 (80:20 비율)
- rename_file.py : 파일 이름을 모두 순차적인 숫자형태로 변경하는 프로그램 (ex. 1.png)
- resize_file.py : 이미지 크기를 원하는 사이즈로 변경하는 프로그램

## 파일 검증
- find_empty_file.py : 아무것도 적혀있지 않은 txt 파일을 찾아내는 프로그램<br>
(json->txt 변경과정에서 json자체에 문제가 있을 경우 빈 txt가 생성됨)
- find_unique_files.py : 2개의 폴더 내 파일이름이 겹치는지 확인하는 코드 (모두 겹쳐야하기에)<br>
(1.png는 있는데 1.txt가 없으면 잘못된 데이터이므로 그것을 확인하기 위해 사용함)

## JSON 파일을 YOLO를 지원하는 TXT파일로 변경하는 용도
### labelme_from_json_to_txt > convert.py
labelme에서 작업한 json 파일을 yolo형식에 맞는 text 파일로 수정하여 저장하는 프로그램
- by. https://github.com/ivder/LabelMeYoloConverter (일부 수정함)
1. dataset에는 수정해야할 데이터셋을 넣음
2. 수정완료시 json_backup 폴더에 기존 json이 들어가게됨
3. 수정완료시 result에서 결과물 파일을 확인할 수 있음.

### 💌 EXAMPLE
### 수정전
```
{
  "version": "5.2.1",
  "flags": {},
  "shapes": [
    {
      "label": "ChickenLeg",
      "points": [
        [
          145.025641025641,
          231.1367521367521
        ],
        [
          443.3162393162393,
          348.2307692307692
        ]
      ],
      "group_id": null,
      "description": "",
      "shape_type": "rectangle",
      "flags": {}
    }
  ],
.....
........
```
### 수정후
```
1 0.48383378317588843 0.4764535537561853 0.4906095366621683 0.1925888439046334
```
## obj_detection 수행하는 용도
### RUN_AI > obj_detection.py
오브젝트 디텍션을 실시간으로 확인해보는 프로그램
- 학습된 데이터를 토대로 실시간으로 객체를 탐지해냄
- 당연하게도 weights, cfg, custom.names파일이 필요함

