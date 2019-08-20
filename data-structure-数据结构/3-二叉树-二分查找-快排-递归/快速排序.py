def sub_sort(list1,low,high):
    x=list1[low]
    while low<high:
        while list1[high]>=x and high >low:
            high-=1
        list1[low]=list1[high]
        while list1[low]<x and high >low:
            low+=1
            list1[high]=list1[low]
        list1[low]=x
    return  low

def quick(list1,low,high):
    if low<high:
        key=sub_sort(list1,low,high)
        quick(list1,low,key-1)
        quick(list1,key+1,high)


l = [3, 7, 6, 5, 8, 3, 4, 2]
quick(l, 0, 7)
print(l)
