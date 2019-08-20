def file_open():
    f=open("dict.txt","r+")
    while True:
        data=f.read(4096)
        if not data:
            break
        print(data)
