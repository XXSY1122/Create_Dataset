from PIL import Image
import os

# 경로설정
path = "C:/Users/user/Desktop/filename" # update this path
files = os.listdir(path)

# 변경하려는 확장자 리스트
change_extensions = ['.jpg', '.jpeg', '.jfif']

for file in files:
    # 파일 확장자가 변경하려는 확장자 리스트에 있는지 확인
    if any(file.lower().endswith(ext) for ext in change_extensions):
        file_path = os.path.join(path, file)
        
        with Image.open(file_path) as img:
            new_file_name = f"{os.path.splitext(file)[0]}.png"
            new_file_path = os.path.join(path, new_file_name)
            
            # (.PNG)새파일로 저장
            img.save(new_file_path, "PNG")
            
            # 원본파일 삭제
            os.remove(file_path)
