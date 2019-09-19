import time
class Father:
    def __init__(self, name):
        print("name: Father")
        self.name = name

    def getName(self):
        return "Father:" + self.name


class Son(Father):
    def __init__(self, name):
        super(Son, self).__init__(name)
        print("name: Son")
        self.name = name

    def getName(self):
        return "Son:" + self.name

    def __add__(self, other):
        return self.name + other.name + "lalal "


son1 = Son("shi")
son2 = Son("qiang")
print(son1 + son2)


localTime = time.asctime(time.localtime(time.time()))

testTime = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime(time.time()))
print(testTime)


