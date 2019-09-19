import threading
import time
import _thread

name = "nihao"
print(name.title())

names = ["shiq", "xiaodi", "liming"]
names.append("haha")
names.insert(0, "lalal")

money = 8031.12 + 6155.84
print("金额为 %d" % money)
print(124000 - money)


print(names)

print(threading.current_thread().name)

del names[1]

for i in names:
    print(i)

print(names)


# for num in range(10 , 20):
#     for i in  range(2,num):
#         if num % i == 0 :
#             j = num % i
#             print("当前 %d 等于 %d * %d" % (num , i , j))
#             break
#
#     else:
#         print(num , "是一个质数")

def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s : %s" % (threadName, time.ctime(time.time())))
try:
    _thread.start_new_thread(print_time, ("thread-1", 1,))
    _thread.start_new_thread(print_time("thread-2", 1))

except:
    print("error")


while 1:
    pass
