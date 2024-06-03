import os
import cv2
import numpy as np
from tqdm import tqdm
                       
if __name__== '__main__':
    lines = open(r'D:\Study\FaceX-Zoo-Custom\data\files\lfw_face_info.txt', 'r').readlines()
    ori_root = r'D:\Study\FaceX-Zoo-Custom\lfw_funneled'

    id = -1
    oldname = ''

    with open('D:\Study\FaceX-Zoo-Custom\lfw_face_train_list.txt', 'w') as writer:
        for i in tqdm(range(len(lines))):
            line = lines[i].strip()
            line_strs = line.split()
            image_name = line_strs[0]
            name = image_name.split('/')[0]
            if oldname != name:
                id=id+1
                oldname = name
            image_path = os.path.join(ori_root, image_name)
            if os.path.exists(image_path):
                writer.writelines(image_name+ " "+str(id)+'\n')
