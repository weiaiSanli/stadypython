import time
import calendar
class Employer:
    def __init__(self , name ,age):
        self.name = name
        self.age = age

    def __del__(self):
        print("我是真正的删除操作!")


employer = Employer("shiq" , 29)
print(employer.name + "---" + str(employer.age))

print(hasattr(employer, 'sex'))
setattr(employer , 'sex' , "nan")
if hasattr(employer , "sex"):
    print(employer.sex)

delattr(employer, 'sex')
print(hasattr(employer , 'sex'))

employer2= employer
employer3 = employer2

print(id(employer) , id(employer2) ,id(employer3))

del employer3
del employer2
del employer

cal  = calendar.month(2019 , 6)
calendar.setfirstweekday(6)
print(cal)

pr = input("请输入数字")
print("当前输入为 %s" % pr)

while 1:
    time.sleep(1)
    print("lla")

