import os
import json
import argparse
import numpy as np


def process_images(data_path, split_rate=0.9):
    '''Convert image information into json files'''
    label_dict = {}
    with open(os.path.join(data_path, "train_label.txt"), 'r') as f:
        lines = f.readlines()
        for one_line_info in lines:
            img_id = one_line_info.split()[0].split('.')[0]
            img_labels = one_line_info.split()[1:]

            # Convert into one-hot
            img_one_hot_labels = np.array([0] * 103)
            for label in img_labels:
                label = int(label) - 1
                img_one_hot_labels[label] = 1

            label_dict[img_id] = img_one_hot_labels

    trainval_data = []
    for one_image in label_dict.keys():
        img_path = os.path.join(data_path, "img_dir/train", one_image + '.jpg')
        data = {"target": label_dict[one_image].tolist(), "img_path": img_path}
        trainval_data.append(data)
    json.dump(trainval_data, open("data/food103/trainval.json", "w"))
    print("Food 103 data preparing finished!")




if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # Usage: --data_path /your/dataset/path/VOCdevkit
    parser.add_argument("--data_path", default="data/food_public/", type=str, help="The path of Food 103 dataset")
    args = parser.parse_args()

    if not os.path.exists("data/food103"):
        os.makedirs("data/food103")

    process_images(args.data_path)
