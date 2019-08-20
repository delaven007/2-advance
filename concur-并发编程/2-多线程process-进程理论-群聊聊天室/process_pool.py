"""
进程池使用
"""
from multiprocessing import Process
from multiprocessing import Pool
from time import sleep,ctime
#进程池事件
def worker(msg):
    sleep(3)
    print(msg)
    return ctime()
#创建进程池
pool=Pool()
#向进程池添加事件
for i in range(10):
    msg="Hello word %d"%i
    r=pool.apply_async(worker,args=(msg,))
#关闭进程池
pool.close()
#回收进程池
pool.join()
print(r.get())      #获取事件函数返回值

