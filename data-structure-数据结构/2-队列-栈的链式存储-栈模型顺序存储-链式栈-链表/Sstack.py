
class StackError(Exception):
    pass


class SStack():
    def __init__(self):
        self._stack=[]

    def is_empty(self):
        return self._stack==[]

    def push(self,elem):
        self._stack.append(elem)

    def pop(self):
        if not self._stack:
            raise StackError("栈为空")
        return self._stack.pop()

    def see_stack_top(self):
        if not self._stack:
            raise StackError('stack is empty')
        return self._stack[-1]
if __name__=="__main__":
    st=SStack()
    st.push(100)
    st.push(150)
    st.push(130)
    while not st.is_empty():
        print(st.pop())

