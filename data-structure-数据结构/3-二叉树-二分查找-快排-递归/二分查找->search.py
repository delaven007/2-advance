"""
search           查找
#对有序数列进行二分查找
"""
def search(list1, key):
    low,high= 0, len(list1) - 1
    while low<=high:
        mid=(low+high)//2
        if list1[mid]<key:
            low=mid+1
        elif list1[mid]>key:
            high=mid-1
        else:
            return mid

l = [0,1,2,3,4,5,6,7,8,9,10,11,12]
print(search(l,10))