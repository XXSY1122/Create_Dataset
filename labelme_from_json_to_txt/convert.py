import os
import json
from PIL import Image

# created this code : https://github.com/ivder/LabelMeYoloConverter

def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

# Configure Paths   
# 데이터셋에 이미지 파일 넣기 (아래 폴더들을 생성하기 바람)
mypath = "./dataset/"
outpath = "./result/"
json_backup ="./json_backup/"

# 메로나는 Class ID = 0 / 닭다리는 Class ID = 1
# 메로나 = Melona
# 닭다리 = ChickenLeg
labels_map = {
    "melona": 0,
    # add other labels if needed
}

# Get input json file list 
json_name_list = [f for f in os.listdir(mypath) if f.endswith(".json")]

# Process 
for json_name in json_name_list:
    txt_name = json_name.rstrip(".json") + ".txt"
    
    # Open input text files 
    txt_path = mypath + json_name
    print("Input:" + txt_path)
    
    with open(txt_path, "r") as txt_file:
        data = json.load(txt_file)

        # Open output text files 
        txt_outpath = outpath + txt_name
        print("Output:" + txt_outpath)
        
        with open(txt_outpath, "w") as txt_outfile:
            # Extract relevant information
            image_path = data['imagePath']
            image_width = data['imageWidth']
            image_height = data['imageHeight']
            shapes = data['shapes']
            
            # Convert the data to YOLO format 
            for shape in shapes:
                label = shape['label']
                points = shape['points']
                
                # Check if label is in our labels map
                if label not in labels_map:
                    print(f"Label {label} not found in labels map. Skipping this shape.")
                    continue
                
                # Get class_id
                class_id = labels_map[label]
                
                # Create box coordinates in YOLO format
                box = [points[0][0], points[1][0], points[0][1], points[1][1]]
                bb = convert((image_width, image_height), box)
                
                # Write to output file
                txt_outfile.write(f"{class_id} {' '.join(map(str, bb))}\n")
    
    os.rename(txt_path, json_backup + json_name)  # move json file to backup folder
