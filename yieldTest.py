# -*- coding:utf-8 -*-
# Author: "Nate"
# Date: 2017/5/12



def consumer(name):
    print("要开始啃骨头了...")
    while True:
        print("\033[31;1m[consumer] %s\033[0m " % name)
        bone = yield
        print("[%s] 正在啃骨头 %s" % (name, bone))


def producer(obj1, obj2):
    obj1.send(None)
    obj2.send(None)
    n = 0
    while n < 5:
        n += 1
        print("\033[32;1m[producer]\033[0m 正在生产骨头 %s" % n)
        obj1.send(n)
        obj2.send(n)



if __name__ == '__main__':
    con1 = consumer("消费者A")
    con2 = consumer("消费者B")
    producer(con1, con2)

#从main函数进入。执行consumer函数，到yield跳出，协程会保存寄存器的状态，接着执行consumer函数，再次跳出执行producer函数，
#producer函数中，send启用生成器，第一次必须传None，不会跳入。while循环中send方法会跳回之前yield跳出的地方
#