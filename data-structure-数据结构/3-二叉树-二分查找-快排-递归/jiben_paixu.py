"""
基本排序算法
"""


# 冒泡排序
# def bubble(list1):
#     # 表达比较轮次
#     for r in range(len(list1) - 1):
#         # 每轮次数
#         for c in range(len(list1) - 1 - r):
#             if list1[c] > list1[c + 1]:
#                 list1[c], list1[c + 1] = list1[c + 1], list1[c]


# 选择排序
# def select(list1):
#     # 外层循环控制论数
#     for i in range(len(list1) - 1):
#         # 内层
#         min = i  # 假定i 为最小值
#         for j in range(i + 1, len(list1)):
#             if list1[min] > list1[j]:
#                 min = j
#         if min != i:
#             list1[i], list1[min] = list1[min], list1[i]
# list1=[5,7,1,4,3,2,9,8]
# select(list1)
# print(list1)


# def put_in(list1):
#     # 外层循环控制轮数
#     for i in range(len(list1) - 1):
#         # 内层
#         min = i  # 假定i为最小值
#         for j in range(i + 1, len(list1)):
#             if list1[min] < list1[j]:
#                 continue
#             if list1[min] > list1[j]:
#                 list1[j], list1[min] = list1[min], list1[j]
#
# list1 = [5, 7, 1, 4, 3, 2, 9, 8]
# put_in(list1)
# print(list1)


# 插入排序
# def insert(list1):
#     for i in range(1, len(list1)):
#         x = list1[i]
#         j = i - 1
#         while j >= 0 and list1[j] > x:
#             list1[j + 1] = list1[j]
#             j -= 1
#         list1[j + 1] = x
#
#
# list1 = [5, 7, 1, 4, 3, 2, 9, 8]
# insert(list1)
# print(list1)





# 快排     low第一个序列号，high最后一个序列号
# 一轮排序
def sub_sort(list1, low, high):
    # 基准数
    x = list1[low]
    while low < high:
        # 后面得数小于X放到前面
        while list1[high] >= x and high > low:
            high -= 1
        list1[low] = list1[high]  # 将数向前甩
        while list1[low] < x and high > low:
            low += 1
        list1[high] = list1[low]
    list1[low] = x  # 将基准数插入
    return low


def quick(list1, low, high):
    if low < high:
        key = sub_sort(list1, low, high)
        quick(list1, low, key - 1)
        quick(list1, key + 1, high)


l = [3, 7, 6, 5, 8, 3, 4, 2]
quick(l, 0, 7)
print(l)
