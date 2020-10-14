import cv2
import sys
from os import listdir
file_path = sys.path[0] + "\\sample_images\\"


def resize_image(file_name):
    img = cv2.imread(file_path + file_name, 1)
    resized_img = cv2.resize(img, (100, 100))
    cv2.imwrite(file_path + 'Resized_' + file_name, resized_img)


for file_name in listdir(file_path):
    resize_image(file_name)
