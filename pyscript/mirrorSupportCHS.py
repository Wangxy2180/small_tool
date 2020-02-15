import cv2 as cv
import os
import numpy as np

# opencv不支持中文路径，百度到的奇技淫巧
def cv_imread(file_path):
    cv_img = cv.imdecode(np.fromfile(file_path,dtype=np.uint8), -1)
    return cv_img

def cv_imwrite(img, path):
    suffix = os.path.splitext(path)[-1]
    cv.imencode(suffix, img)[1].tofile(path)


print("该文件产生镜像翻转文件(仅支持jpg)")
path = input("请输入文件夹的路径(请注意：若使用windows下 复制路径 功能，请去掉字符串两边的引号)\n"
             "该文件支持中文路径\n"
             "该文件会默认将所有图像转为横置，若有特殊要求，请使用英文路径版\n")
print(path)
mirrorType = eval(input("请输入翻转类型\n-1:中心翻转\n1:左右翻转\n0：上下旋转\n"))
mirrorDictType = {-1: "Cen",
                  1: "LR",
                  0: "UD"}

jpgMirrorNameFile = "jpgNameFile_"+mirrorDictType[mirrorType]+".txt"
jpgMirrorNameFilePath = os.path.join(path,jpgMirrorNameFile)
print(jpgMirrorNameFilePath)
fp = open(jpgMirrorNameFilePath, 'w')
# newFolder = path+"\\"+mirrorDictType[mirrorType]
newFolder = os.path.join(path, mirrorDictType[mirrorType])
os.mkdir(newFolder)


fileList = os.listdir(path) # 该文件夹下所有的文件（包括文件夹）
for file in fileList:   # 遍历所有文件
    oldDir = os.path.join(path, file)   # 原来的文件路径
    if os.path.isdir(oldDir):   # 如果是文件夹则跳过
        continue
    fileName = os.path.splitext(file)[0]   # 文件名
    fileType = os.path.splitext(file)[1]   # 文件扩展名
    if fileType == ".jpg":
        newFileName = fileName+"_"+mirrorDictType[mirrorType]
        newDir = os.path.join(newFolder,newFileName+fileType)
        # print(oldDir)
        # opencv
        img = cv_imread(oldDir)
        img2 = cv.flip(img, mirrorType, dst=None)
        # 1左右翻转 0中心旋转  -1上下翻转
        img3 = cv.resize(img2, (800, 450))
        cv.imshow("123",img3)
        cv.waitKey(30)
        cv_imwrite(img2,newDir)
        fp.write(os.path.splitext(newFileName)[0]+"\n")
        print(newDir)
fp.close()
print("运行结束")
# 该文件产生镜像翻转，通过奇技淫巧可以支持中文路径
# 包含三种模式，左右，上下，以及中心
# 生成的文件将存会在源文件夹中生成一个以翻转方式命名的新文件夹中