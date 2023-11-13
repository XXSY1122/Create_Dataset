import os

# 폴더내 데이터 이름이 겹치는지 안겹치는지 확인하는 코드 (참고로 모두 겹쳐야함)
# ex. 1.png / 1.txt or 1.png / none.txt 의 유무를 파악

# 비교 용도의 각각의 폴더 경로를 지정
path_A = 'c:\\Users\\ksl97\\Downloads\\누가바\\NUGABAR1'
path_B = 'c:\\Users\\ksl97\\Downloads\\누가바\\NUGABAR1img'


def find_and_print_unique_files(folderA, folderB):
    # A폴더와 B폴더에서 파일 이름을 가져옴 (확장자는 무시함)
    files_in_A = {os.path.splitext(file)[0] for file in os.listdir(folderA)}
    files_in_B = {os.path.splitext(file)[0] for file in os.listdir(folderB)}

    # A폴더와 B폴더에서 겹치지 않는 파일 찾기
    unique_files = (files_in_A - files_in_B).union(files_in_B - files_in_A)

    if unique_files:
        print("Non-overlapping files:")
        for file in unique_files:
            print(file)
    else:
        print("All files overlap.")

find_and_print_unique_files(path_A, path_B)
