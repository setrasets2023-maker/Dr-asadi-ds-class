class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    # ✅ متد اولویت‌دار کردن پشته
    def prioritize(self):
        temp = []
        while not self.is_empty():
            temp.append(self.pop())

        temp.sort(reverse=True)   # اولویت بالاتر = عدد بزرگ‌تر

        for x in temp:
            self.push(x)






s = Stack()
s.push(3)
s.push(1)
s.push(5)
s.push(2)

s.prioritize()
print(s.stack)   # [1, 2, 3, 5]  ← 5 بالای پشته
