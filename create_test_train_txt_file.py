import os

# This function will create train.txt and test.txt files
def trainNtestFilesCreater(dataSetPath, mappingPath, train_size=0.80):
    listD = os.listdir(dataSetPath)
    # filtering the images
    images = [file for file in listD if file.split(".")[1] == "png"]
    # getting the training size
    trainS = int(len(images) * train_size)

    # creating txt files
    train = open("train.txt", "wt")
    test = open("test.txt", "wt")

    counter = 1
    for file in images:
        if counter <= trainS:
            # writing in train.txt file
            train.writelines(f"{mappingPath}/{file}\n")
        else:
            # writing in text.txt file
            test.writelines(f"{mappingPath}/{file}\n")
        counter += 1
    train.close()
    test.close()
    print(f"{counter} files processed")


# 데이터셋 현재 경로
dataSetPath = r"C:/Users/ksl97/Desktop\dataset/labelme_from_json_to_txt/result"
# test.txt train.txt에 기입될 경로 (코랩을 사용할땐 아래처럼 '/content/gdrive/MyDrive/본인폴더/'로 지정함)
mappingPath = "/content/gdrive/MyDrive/custom_data/images"

# calling creater function to generate files
trainNtestFilesCreater(dataSetPath, mappingPath, train_size= 0.80)
