def search(list1,key):
    low,high=0,len(list1)-1
    while low<high:
        mid=low+high//2
        if list1[mid]<key:
            low=mid+1
        if list1[mid]>key:
            high=mid-1
        else:
            return mid
