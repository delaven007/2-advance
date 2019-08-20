"""
search.py 基本查找方法训练
"""
#　对有序数列进行二分查找
def search(list_,key):
  low,high = 0,len(list_) - 1
  while low <= high:
    mid = (low + high) // 2
    if list_[mid] < key:
      low = mid + 1
    elif list_[mid] > key:
      high = mid - 1
    else:
      return mid

l = [1,2,3,4,5,6,7,8,9,10]
print("Key index is:",search(l,12))







