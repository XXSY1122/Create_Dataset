from tensorflow.keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img
import os
import scipy

# 경로 설정
input_path = "/Users/sy/Desktop/Create_Dataset/닭다리완성본"  # Update this path
output_path = "/Users/sy/Desktop/Create_Dataset/chicken_aug"  # Update this path
os.makedirs(output_path, exist_ok=True)

# ImageDataGenerator
# 미세 조정 가능 (0.2 이상의 값을 넣어도 됨. 단, 값이 클수록 이미지 전체적인 왜곡이 심해질 수 있음)
datagen = ImageDataGenerator(
    rotation_range=10,  # 회전각도
    width_shift_range=0.05,  # 폭조정
    height_shift_range=0.05,  # 높이조정
    shear_range=0.05,  # 왜곡조정 (이부분은 조정을 심하게 하지 않는걸 추천)
    zoom_range=0.05,  # 확대/축소조정
    horizontal_flip=False,  # 수평뒤집기 ON상태 (원하지 않는다면 False값 대입)
    fill_mode='nearest'  # 채우기 모드를 '가장 가까운'으로 설정 
    # (즉, 확대/축소로 인해 이미지 크기가 변형될때 빈 픽셀공간이 생기면 그 픽셀에 가장 가까운 값에 위치한 색상을 넣음)
)

files = os.listdir(input_path)
augment_per_image =  627 // len(files) # 5
# 원하는 파일수 // 현재파일수 (즉, 이 코드에선 기존 261개의 파일의 5배인 1305개로 늘리게됨)

for file in files:
    img = load_img(os.path.join(input_path, file))
    x = img_to_array(img) # 로드된 이미지를 넘파이 배열로 변환
    x = x.reshape((1,) + x.shape) # 이미지 배열의 형태를 4D 형태로 변환 (1, height, width, channels)

    i = 0
    for batch in datagen.flow(x, batch_size=1, save_to_dir=output_path, save_prefix='aug', save_format='jpeg'):
        i += 1
        if i >= augment_per_image:
            break
        # i가 augment_per_image값을 넘기면 루프빠져나감 (즉, i가 1305개 되면 빠져나감)
