import threading
import time

threadLock = threading.Lock()
lists = [0, 0, 0, 0, 0, 0, 0, 0, 0]


class myThread(threading.Thread):

    def __init__(self, threadId, name, delay):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
        self.delay = delay

    def run(self):
        print("开始线程 %s " % self.name)
        # 获取锁对象
        threadLock.acquire()
        print_time(self.name, self.delay, lists.__len__())
        threadLock.release()

    def __del__(self):
        print(self.name + "线程结束")



def print_time(threadName, delay, counter):
    print(counter)
    while counter:
        time.sleep(delay)
        lists[counter - 1] += 1
        print("[%s] %s 修改第 %d 个值，修改后值为:%d" % (time.ctime(time.time()), threadName, counter, lists[counter - 1]))
        counter -= 1


thread = []
thread1 = myThread(1, "thread_01", 1)
thread2 = myThread(2, "thread_02", 2)

thread1.start()
thread2.start()

thread.append(thread1)
thread.append(thread2)

for t in thread :
    t.join()

print("Main结束")

