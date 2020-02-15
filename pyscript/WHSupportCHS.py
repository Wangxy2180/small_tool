import cv2 as cv
import numpy as np
import os

# opencv不支持中文路径，百度到的奇技淫巧
def cv_imread(file_path):
    cv_img = cv.imdecode(np.fromfile(file_path,dtype=np.uint8), -1)
    return cv_img

def cv_imwrite(img, path):
    suffix = os.path.splitext(path)[-1]
    cv.imencode(suffix, img)[1].tofile(path)

path = input("请输入文件路径 支持中文路径 只支持jpg格式\n"
             "注意：若使用windows的“复制路径”功能，请删去路径的双引号\n")

fileLists = os.listdir(path)
for file in fileLists:
    thisDir = os.path.join(path,file)
    if os.path.isdir(thisDir):
        continue
    img = cv_imread(thisDir)
    fileType = os.path.splitext(file)[1]
    fileName = os.path.splitext(file)[0]
    if fileType == ".jpg":
        # img2 = cv.resize(img,(int(img.shape[1]/5),int(img.shape[0]/5)))
        # cv.imshow("123",img2)
        # cv.waitKey(30)
        cv_imwrite(img,thisDir)
        print(thisDir)
print("结束")

# 旋转图像，将竖图旋转为横图
# 通过奇技淫巧支持中文路径
