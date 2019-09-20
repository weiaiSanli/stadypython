import os
import time
import threading
import shutil


class SignApkThread(threading.Thread):
    def __init__(self, fileDir, osCmd):
        threading.Thread.__init__(self)
        self.fileDir = fileDir
        self.osCmd = osCmd

    def run(self):
        lock.acquire()
        print("开始打包!!! 地址为 %s" % self.fileDir)
        os.chdir(_dict_path['apkFileDir'])
        os.system(self.osCmd)
        apkPath = getApkName(self.fileDir)
        print("打包以后的地址为: " + apkPath)
        copyFile(self.fileDir + "\\" + apkPath, copyFilePath + "\\" + apkPath)
        lock.release()


time = '123.000'
print(float(time))


def getApkName(apkDir) -> str:
    editTime = 0.0
    lastEditFile = ""
    for path in os.listdir(apkDir):
        if path.endswith(".apk"):
            itemTime = float(os.path.getmtime(apkDir + "\\" + path))
            if itemTime > editTime:
                editTime = itemTime
                lastEditFile = path
    return lastEditFile


# 复制文件到指定位置
def copyFile(oldFile, newFile):
    shutil.copy(oldFile, newFile)


# 删除文件夹
def del_path(delPath):
    if not os.path.exists(delPath):
        return
    if os.path.isfile(delPath):
        os.remove(delPath)
        print("删除文件 %s" % delPath)
    else:
        items = os.listdir(delPath)
        for f in items:
            o_path = os.path.join(delPath, f)
            if os.path.isdir(o_path):
                del_path(o_path)
            else:
                os.remove(o_path)
                print("删除文件 %s" % o_path)
        print("删除文件夹中的所有文件成功!")


def addThread(fileDir, osCmd):
    threadRelease = SignApkThread(fileDir, osCmd)  # 打包tesing版本包
    threadRelease.start()
    threads.append(threadRelease)


_dict_path = {}


def readFile(filePath):
    with open(filePath, 'r') as fileLines:
        for line in fileLines:
            key, value = line.rstrip().split('=')
            _dict_path[key.strip()] = value.strip()


threads = []
lock = threading.Lock()
readFile('signApkFile.txt')
# 文件最终存储位置
copyFilePath = _dict_path['copyFilePath']
addressBaseDir = _dict_path['addressBaseDir']
addressReleaseDir = addressBaseDir + "release"
addressTesingDir = addressBaseDir + "tesing"
addressDemoDir = addressBaseDir + "demo"

isDelete = input("请输入是否删除原有文件 \n Y/N :")
if isDelete.lower() == 'y':
    del_path(copyFilePath)  # 删除全部已复制文件
else:
    pass
hasPackage = True
_trump_gradle = ("gradlew assembleTesing", "gradlew assembleDemo", "gradlew assembleRelease")
_trump_dir = (addressTesingDir, addressDemoDir, addressReleaseDir)


def signTypeApk(signPosition):
    addThread(_trump_dir[signPosition], _trump_gradle[signPosition])


_trump_types = ("tesing", "demo", "release", "all")

while hasPackage:
    hasPackage = False
    packageType = input("请输入需要打包的环境 \n demo:预上线  release : 正式环境 \n tesing : 测试  all : 所有环境 \n")

    clickPosition = -1
    for position, item in enumerate(_trump_types):
        if packageType == item:
            clickPosition = position
            break

    print("position %s" % clickPosition)
    if position < 0:
        hasPackage = True
    elif position == 3:
        pass
        signTypeApk(0)
        signTypeApk(1)
        signTypeApk(2)
    else:
        pass
        signTypeApk(position)

for t in threads:
    t.join()
print("打包完成!")
