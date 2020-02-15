import cv2 as cv
import os

path = input("输入需要压缩图片的文件夹 只支持英文路径\n"
             "注意：会覆盖源文件\n")

fileList = os.listdir(path)
for file in fileList:
    thisPath = os.path.join(path,file)
    img = cv.imread(thisPath)
    cv.imwrite(thisPath, img)
print("done")

# 对大图片进行压缩
# 单纯的通过opencv进行读写
# 会覆盖原图片
# 只支持英文路径