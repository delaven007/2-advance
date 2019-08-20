from multiprocessing import Process
from time import sleep
def worker(sec,name):
    for i in range(3):
        sleep(sec)
        print("I'm %s "%name)
        print("I'm working..")

p=Process(target=worker,args=(2,"Hony"))
# p=Process(target=worker,kwargs={"name":"Abby","sec":5})
p.start()
p.join()