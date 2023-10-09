import os

# 전체 파일명을 숫자로 변경하는 프로그램
# 이미지 파일 이름이 뒤죽박죽 상태일때 숫자 1.2.3.4.5...순으로 전체 변경해준다. 

# 이미지 파일 경로
path = "C:/Users/ksl97/Desktop/메로나"

files = os.listdir(path)
files.sort()

# Step 1: Rename files to temporary names
for idx, file in enumerate(files):
    old_file_path = os.path.join(path, file)
    # Construct the new file name with a temporary prefix
    new_file_name = f"tmp_{idx + 1}.png"
    new_file_path = os.path.join(path, new_file_name)
    os.rename(old_file_path, new_file_path)

# Get a list of all temporary files in the directory
tmp_files = [file for file in os.listdir(path) if file.startswith("tmp_")]

# Sort temporary files by name
tmp_files.sort()

# Step 2: Rename temporary files to final names
for idx, file in enumerate(tmp_files):
    old_file_path = os.path.join(path, file)
    # Construct the final file name without the temporary prefix
    new_file_name = f"{idx + 1}.png"
    new_file_path = os.path.join(path, new_file_name)
    os.rename(old_file_path, new_file_path)

