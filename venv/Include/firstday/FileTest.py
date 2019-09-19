import os
import json
address = "E:\\work\\gc_details\\logs\\"

file = open(address + "test.txt", "a")
print(file.name)
file.write("nihao a ,shaonian")
file.close()

fo = open(address + "test.txt", "r+")
str = fo.read(10)
position = fo.tell()
print("当前文件位置 : ", position)
str2 = fo.read(10)
print(str)
print(str2)
fo.close()

# os.renames(address + "test.txt" , address + "new.txt")
os.rmdir(address + "shi")
os.mkdir(address + "shi")
print(os.getcwd())

document = open("file.txt", "w+")
print("文件名", document.name)
document.write("这是一个测试文件 \n welcome")
document.flush() # 刷新缓存一遍读取不是乱码
print(document.tell())
document.seek(os.SEEK_SET)
context = document.read()
print(context)
document.close()

with open("file.txt", 'r') as f:
    print(f.read())

data = {
    'no' : 1,
    'name' : 'Runoob',
    'url' : 'http://www.runoob.com'
}
jsonStr = json.dumps(data)
print("字典类型" , data)
print("字典类型" , repr(data))
print("json类型" , jsonStr)

def make(*names):
    for name in names:
        print("当前任务为:" , name)

make("shiq")
make("shiq" , "hah" , "yao")

