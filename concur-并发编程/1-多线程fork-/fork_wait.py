"""
wait 处理僵尸
"""
import os
pid =os.fork()
if pid < 0:
    print("Error")
elif pid == 0:
    print("Child Process",os.getppid())
    os._exit(5)                        # 乘以256
else:
    p, status=os.wait()       #阻塞等待子进程退出
    print("P:",p)
    #还原退出状态
    print("Status:",os.WEXITSTATUS(status))
    while  True:
        pass
