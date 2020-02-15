import os

path = input("请输入文件夹路径(只支持jpg格式)\n")
fileLists = os.listdir(path)

txtName = "newName.txt"
txtPath = os.path.join(path,txtName)
fp = open(txtPath,'w')
for file in fileLists:
    filePath = os.path.join(path,file)
    if os.path.isdir(filePath):   # 如果是文件夹则跳过
        continue
    fileName = os.path.splitext(file)[0]
    fileType = os.path.splitext(file)[1]
    fp.write(fileName+"\n")
fp.close()
#此文件用来生成文件夹中的文件名列表
#不含文件名的格式部分
#生成的txt文件名为newName.txt
#如对于文件夹中1.jpg--100.jpg
#则在txt中生成1-100序号，每个序号占一行
#1
#2
#···
#100