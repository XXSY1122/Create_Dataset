from PIL import Image
import os

# 이미지 사이즈 수정 (이 코드에선 608x608 사이즈)
def resize_images(input_dir, output_dir, new_size=(608, 608)):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.png')):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)
            
            try:
                with Image.open(input_path) as img:
                    resized_img = img.resize(new_size, Image.BILINEAR)
                    resized_img.save(output_path)
            except Exception as e:
                print(f"Error processing {filename}: {str(e)}")

# 사용 예
input_directory = '/Users/sy/Desktop/Create_Dataset-main/닭다리'  # 원본 이미지가 있는 디렉터리 경로
output_directory = '/Users/sy/Desktop/Create_Dataset-main/닭다리수정'  # 크기를 변경한 이미지를 저장할 디렉터리 경로

resize_images(input_directory, output_directory)
