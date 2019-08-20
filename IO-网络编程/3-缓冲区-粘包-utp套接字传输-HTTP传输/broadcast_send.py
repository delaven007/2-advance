#发送广播
from socket import *
import time

#广播地址
dest=("localhost",6666)
s=socket(AF_INET,SOCK_DGRAM)
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

data="""asdfk
********************************
tarena@tarena:~$ ifconfig
enp2s0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 172.40.74.131  netmask 255.255.255.0  broadcast 172.40.74.255
        inet6 fe80::4105:814d:1719:4ae  prefixlen 64  scopeid 0x20<link>
        ether fc:aa:14:37:99:51  txqueuelen 1000  (以太网)
        RX packets 62818  bytes 25438216 (25.4 MB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 65809  bytes 10980720 (10.9 MB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (本地环回)
        RX packets 28960  bytes 4685374 (4.6 MB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 28960  bytes 4685374 (4.6 MB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

tarena@tarena:~$ ^C
tarena@tarena:~$ 

--------------------------------
"""
while True:
    time.sleep(1)
    s.sendto(data.encode(),dest)
