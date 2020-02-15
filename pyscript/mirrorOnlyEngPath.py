import cv2 as cv
import os


print("该文件产生镜像翻转文件(仅支持jpg)")
path = input("请输入文件夹的路径(请注意：若使用windows下 复制路径 功能，请去掉字符串两边的引号)\n"
             "该文件不支持中文路径！！！\n")
print(path)
mirrorType = eval(input("请输入翻转类型\n-1:中心翻转\n1:左右翻转\n0：上下旋转\n"))
mirrorDictType = {-1: "Cen",
                  1: "LR",
                  0: "UD"}

jpgMirrorNameFile = "jpgNameFile_"+mirrorDictType[mirrorType]+".txt"
jpgMirrorNameFilePath = os.path.join(path,jpgMirrorNameFile)
print(jpgMirrorNameFilePath)
fp = open(jpgMirrorNameFilePath,'w')
newFolder = os.path.join(path,mirrorDictType[mirrorType])
print(newFolder)
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
        # opencv
        img = cv.imread(oldDir, 5)
        img2 = cv.flip(img, mirrorType, dst=None)
        # 1左右翻转 0中心旋转  -1上下翻转
        img3 = cv.resize(img2, (800, 450))
        # cv.imshow("123",img3)
        # cv.waitKey(30)
        cv.imwrite(newDir, img2)
        fp.write(os.path.splitext(newFileName)[0]+"\n")
        print(newDir)
fp.close()
print("运行结束")
# 该文件产生镜像翻转，只支持英文路径
# 包含三种模式，左右，上下，以及中心
# 生成的文件将存会在源文件夹中生成一个以翻转方式命名的新文件夹中