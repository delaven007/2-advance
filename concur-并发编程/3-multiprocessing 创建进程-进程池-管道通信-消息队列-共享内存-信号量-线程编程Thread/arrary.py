from multiprocessing import Process,Array

#创建共享内存空间
# shm = Array("i",[1,2,3])
# shm=Array("i",3)    #开辟3个类型的空间
shm=Array("c","hello".encode())   #字节串
def fun():
    #共享内存对象可迭代
    for i in shm:
        print(i)
    shm[1]="S".encode()
p = Process(target=fun)
p.start()
p.join()

for i in shm:
    print(i)
print(shm.value)     #打印字节串
