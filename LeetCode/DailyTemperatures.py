from collections import deque

class StackItem:
    def __init__(self, index, value):
        self.index = index
        self.value = value
    def __str__(self):
        return self.index + ' ' + str(self.value)

class Solution:
    def dailyTemperatures(self, T):
        result = [0]*len(T)
        indexes = []
        stack = deque()

        for i in range(0, len(T)):
            indexes.append(i)
        
        for j in range(len(T)-1, -1, -1):
            item = StackItem(j, T[j])
            if (len(stack) == 0):
               stack.append(item)
            else:
                tmp = stack.pop()
                while (item.value >= tmp.value and len(stack) > 0):
                    tmp = stack.pop()
                if (item.value >= tmp.value):
                    stack.append(item)
                    result[j] = item.index - j
                else:
                    stack.append(tmp)
                    result[j] = tmp.index - j
                
                stack.append(item)
        return result

    def testStack(self):
        stack = deque()
        stack.append(StackItem("a1", 0))
        stack.append(StackItem("a2", 1))
        stack.append(StackItem("a3", 2))
        x = stack.pop()
        print(str(x))
        stack.append(x)
        return

s = Solution()
dt = [89,62,70,58,47,47,46,76,100,70]
print(s.dailyTemperatures(dt))
# s.testStack()

