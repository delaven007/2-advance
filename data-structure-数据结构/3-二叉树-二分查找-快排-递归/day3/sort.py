"""
基本排序算法训练
"""

#　冒泡
def bubble(list_):
  #　外层循环表达比较多少轮
  for i in range(len(list_) - 1):
    #内层循环把控比较次数
    for j in range(len(list_) - 1 - i):
      if list_[j] > list_[j + 1]:
        list_[j],list_[j + 1] = \
          list_[j + 1],list_[j]

# 选择
def select(list_):
  # 外层循环控制比较多少轮
  for i in range(len(list_) - 1):
    min = i #　假定list_[i] 为最小值
    for j in range(i+1,len(list_)):
      if list_[min] > list_[j]:
        min = j
    #　如果ｉ不是最小值则交换
    if min != i:
      list_[i],list_[min] = \
        list_[min],list_[i]

#　插入
def insert(list_):
  #　控制每次ｘ选取的待插入数值
  for i in range(1,len(list_)):
    x = list_[i]  #　选取待处理的数
    j = i - 1
    while j >=0 and list_[j] > x:
      list_[j + 1] = list_[j]
      j -= 1
    list_[j + 1] = x

# 完成一轮排序过程
def sub_sort(list_,low,high):
  #　基准数
  x = list_[low]
  while low < high:
    #　后面的数小于ｘ放到前面的空位
    while list_[high] >= x and high > low:
      high -= 1
    list_[low] = list_[high] #　将数往前甩
    while list_[low] < x and low < high:
      low += 1
    list_[high] = list_[low]
  list_[low] = x #　将基准数插入
  return low


#　快排 low 第一个数序列号　high 最后一个数序列号
def quick(list_,low,high):
  if low < high:
    key = sub_sort(list_,low,high)
    quick(list_,low,key - 1)
    quick(list_, key+1, high)


l = [3,7,6,5,8,3,4,2]
# bubble(l)
# select(l)
# insert(l)
quick(l,0,7)
print(l)

