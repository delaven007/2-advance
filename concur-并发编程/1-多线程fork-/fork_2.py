import os
pid=os.fork()
print("----------------------")
a=1
while True:
    if pid<0:
        print("Create process failed")
    elif pid==0:
        print("new process")
        print(a)
    else:
        print("Old process")
    print("a:",a)