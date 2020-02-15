import os
print("此文件用于文件批量排序命名(.jpg)(不进行格式修改)并将文件名写入txt")
path = input("请输入文件夹的路径(请注意：若使用windows下 复制路径 功能，请去掉字符串两边的引号)\n")
print(path)
prefix = input("请输入文件命名前缀\n")
num = eval(input("请输入起始序号\n"))
orderCapacity=eval(input("请输入命名序号的总位数\n"))
jpgNameFile = "jpgNameFile.txt"
jpgNameFilePath = os.path.join(path,jpgNameFile)
print(jpgNameFilePath)
fp = open(jpgNameFilePath,'w')
for file in os.listdir(path):
    oldDir = os.path.join(path,file)
    if os.path.isdir(oldDir):
        continue
    fileType = os.path.splitext(file)[1]
    fileName = os.path.splitext(file)[0]
    newFileName = prefix+"_"+str(num).zfill(orderCapacity)+fileType
    newDir = os.path.join(path,newFileName)
    if fileType == ".jpg":
        os.rename(oldDir,newDir)
        print(file + " -> " + newFileName)
        fp.write(os.path.splitext(newFileName)[0]+"\n")
    num = num+1
fp.close()

# 对文件进行批量名
# 输入文件名前缀，其实序号，以及序号的位数
# 同时生成文件名（不包括后缀）的序列文件，也就是fileNameTxt.py干的事
