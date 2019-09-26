fileName = "pi_million_digits.txt"
with open(fileName, 'r') as file_object:
    lines = file_object.readlines()

piStr = ""
for line in lines:
    piStr += line.rstrip()

birthday = input("请你输入生日:\n")

if birthday in piStr:
    print("你的生日在其中")
else:
    print("你的生日不在其中")

allNum = 124000
jianm = 7939.40 + 6064.11
print(allNum - jianm)
