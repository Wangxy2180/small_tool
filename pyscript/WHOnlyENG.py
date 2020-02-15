import cv2 as cv
import numpy as np
import os
path = input("请输入文件路径 不支持中文路径 只支持jpg格式\n"
             "注意：若使用windows的“复制路径”功能，请删去路径的双引号\n")

fileLists = os.listdir(path)
for file in fileLists:
    thisDir = os.path.join(path,file)
    if os.path.isdir(thisDir):
        continue
    img = cv.imread(thisDir)
    fileType = os.path.splitext(file)[1]
    fileName = os.path.splitext(file)[0]
    if fileType == ".jpg":
        if img.shape[1] > img.shape[0]:  # 宽大于高，跳过
            continue
        print("旋转图像"+file)
        img90 = np.rot90(img)
        cv.imwrite(thisDir,img90)
print("结束")
# 旋转图像，将竖图旋转为横图
# 只支持英文路径
