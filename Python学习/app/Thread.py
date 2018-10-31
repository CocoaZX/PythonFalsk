import threading
from  time import ctime,sleep


#、join ()方法：主线程A中，创建了子线程B，并且在主线程A中调用了B.join()，那么，主线程A会在调用的地方等待，直到子线程B完成操作后，才可以接着往下执行，那么在调用这个线程时可以使用被调用线程的join方法。
#原型：join([timeout])，里面的参数时可选的，代表线程运行的最大时间，即如果超过这个时间，不管这个此线程有没有执行完毕都会被回收，然后主线程或函数都会接着执行的。


#setDaemon()方法。主线程A中，创建了子线程B，并且在主线程A中调用了B.setDaemon()，这个的意思是，把主线程A设置为守护线程，这时候，要是主线程A执行结束了，就不管子线程B是否完成，一并和主线程A退出.这就是setDaemon方法的含义，
# 这基本和join是相反的。此外，还有个要特别注意的：必须在start() 方法调用之前设置。


#join会等待,setDaemon 会依赖

def music(func):
    for i in range(2):
        print ("I was listening to %s. %s" %(func,ctime()))
        sleep(1)

def move(func):
    for i in range(2):
        print ("I was at the %s! %s" %(func,ctime()))
        sleep(5)

threads = []
#注意关键字是target=music，因为参数是函数本身，而不是调用函数target=music()并使用返回值
t1 = threading.Thread(target=music,args=(u'爱情买卖',))
threads.append(t1)
t2 = threading.Thread(target=move,args=(u'阿凡达',))
threads.append(t2)


def build(type, value):
    return type(value)

if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()

    t.join()

    print ("all over %s" %ctime())