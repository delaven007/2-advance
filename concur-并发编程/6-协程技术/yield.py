def fun():
  print("启动生成器")
  yield 1
  print("生成器完成")

#　迭代对象
g = fun()
print(g.__next__())
print(g.__next__())


