from glob import glob
from PIL import Image
import os
import re
import matplotlib.pyplot as plt
import cv2
import shutil

# 파일 이름 변경 코드
# 문자형때문에 1.png / 1.txt -> 1.png / 30.txt 으로 바뀌던 문제를 해결한 코드
# 파일명 모두, 숫자를 기준으로 정렬하여 바꿈

n=2476 # 원하는 첫번째 파일명 (ex. 2476이면 2476.png / 2476.txt 이 시작파일)

def extract_number(filename):
    numbers = re.findall(r'\d+', filename)
    return int(numbers[0]) if numbers else None

#JAWSBAR
#p1=f'C:\\Users\\ksl97\\Downloads\\nugabar\\NUGABAR2\\*.png'
p1=f'C:\\Users\\ksl97\\Downloads\\ok\\OKDONGJA2\\*.png'
p2=f'C:\\Users\\ksl97\\Downloads\\ok\\OKDONGJA2\\*.txt'

img_list = glob(p1)
label_list = glob(p2)

img_list.sort(key=extract_number)
label_list.sort(key=extract_number)

label_name_list=[]

for a in label_list:
    base_name = os.path.basename(a)
    file_name, _ = os.path.splitext(base_name)
    label_name_list.append(file_name)

to_remove = []

for d in img_list:
    base_name = os.path.basename(d)
    file_name, _ = os.path.splitext(base_name)
    if file_name not in label_name_list:
        to_remove.append(d)

for item in to_remove:
    img_list.remove(item)

for i in range(len(img_list)):

    new_img_path=f"C:\\Users\\ksl97\\Downloads\\images\\{n}.png"
    new_label_path=f"C:\\Users\\ksl97\\Downloads\\labels\\{n}.txt"

    img=cv2.imread(img_list[i])
    if img is None:
        print(f"Failed to read image: {img_list[i]}")
        continue

    cv2.imwrite(new_img_path,img)

    shutil.copy(label_list[i], new_label_path)
    n+=1

print(len(img_list), len(label_list), n,end=' ')
