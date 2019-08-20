from day1.my_Linklist.bll import Linklist


if __name__ =="__main__":
    link = Linklist()
    l = [1, 2, 3, 4, 5, 6]
    link.init__list(l)
    link.show()  # 遍历
    print(link.get_lenth())
    link.append(7)
    link.show()
    link.insert(5, 80)
    link.show()
    link.delete(2)
    link.show()
    link.get_item(4)
    print(link.clear())
