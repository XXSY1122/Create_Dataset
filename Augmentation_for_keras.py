from tensorflow.keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img
import os

# Specify the path where the images are stored
input_path = "C:/Users/ksl97/Desktop/crawled"  # Update this path
output_path = "C:/Users/ksl97/Desktop/crawleddone"  # Update this path

# Make sure the output path exists, if not create it
os.makedirs(output_path, exist_ok=True)

# Creating a more gentle ImageDataGenerator
datagen = ImageDataGenerator(
    rotation_range=10,  # Even more reduced rotation
    width_shift_range=0.05,  # Even more reduced width shift
    height_shift_range=0.05,  # Even more reduced height shift
    shear_range=0.05,  # Even more reduced shear range
    zoom_range=0.05,  # Even more reduced zoom
    horizontal_flip=True,  # Kept horizontal flip
    fill_mode='nearest'  # Kept fill mode as nearest
)

files = os.listdir(input_path)
augment_per_image = 1305 // len(files) # 1장당 5개이미지 더 생성함 (기존261x변형5)

for file in files:
    img = load_img(os.path.join(input_path, file))
    x = img_to_array(img)
    x = x.reshape((1,) + x.shape)

    i = 0
    for batch in datagen.flow(x, batch_size=1, save_to_dir=output_path, save_prefix='aug', save_format='jpeg'):
        i += 1
        if i >= augment_per_image:
            break
