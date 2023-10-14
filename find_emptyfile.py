import os
# 아무 내용이 없는 txt 파일을 찾아 알려줌


# 탐색할 폴더 경로 지정
folder_path = "C:/Users/ksl97/Downloads/ChickenLeg"
#C:\Users\ksl97\Downloads\fnd

# 폴더 내의 모든 파일을 가져옴
all_files = os.listdir(folder_path)

# .txt 파일만 필터링
txt_files = [f for f in all_files if f.endswith('.txt')]

# 내용이 없는 파일의 이름을 저장할 리스트
empty_files = []

# 각 .txt 파일을 순회합니다.
for file in txt_files:
    file_path = os.path.join(folder_path, file)
    # 파일을 열고 내용을 확인합니다.
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        # 파일 내용이 비어있다면, empty_files 리스트에 추가합니다.
        if content.strip() == "":
            empty_files.append(file)

# 내용이 없는 파일이 있다면, 파일명을 출력합니다.
if empty_files:
    print(f"{', '.join(empty_files)} empty.")
else:
    print("Good! All of is ok.")
