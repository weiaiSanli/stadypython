import threading
import time

exitFlag = 0

threadLock = threading.Lock()
threads = []


class myThread(threading.Thread):  # 继承自父类的Thread
    def __init__(self, threadID, name, count):
        threading.Thread.__init__(self)
        self.name = name
        self.threadID = threadID
        self.count = count

    def run(self):  # 运行程序
        # threadLock.acquire()
        print("开始执行" + self.name)
        print_time(self.name, self.count, 5)
        print("退出" + self.name)
        # threadLock.release()


def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1


# 创建新线程
thread1 = myThread(1, "Thread-01", 1)
thread2 = myThread(2, "Thread-02", 2)

# 开启县城管
thread1.start()
thread2.start()

threads.append(thread1)
threads.append(thread2)

strName = "Yy"
print(strName.lower() + "嘿嘿")

for t in threads:
    t.join()

print("退出主程序")
