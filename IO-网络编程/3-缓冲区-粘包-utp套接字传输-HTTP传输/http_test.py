"""
http 请求响应
"""
from  socket import *
s=socket()
s.bind(("localhost",9999))
s.listen(5)
c,addr=s.accept()
print(addr)

data="""HTTP/1.1 200 OK
Content-Type:text/html
<h1>Hello KITTY</h1>
"""

c.recv(4096)
c.send(data.encode())
c.close()
s.close()