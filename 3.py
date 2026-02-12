class Stack:
    def __init__(self, size=5):
        self.size = size
        self.is_static = True   # شروع به صورت استاتیک
        self.stack = [None] * size
        self.top = -1

    def push(self, x):
        if self.is_static:
            if self.top == self.size - 1:
                print("Stack Overflow (Static)")
                return
            self.top += 1
            self.stack[self.top] = x
        else:
            self.stack.append(x)

    def pop(self):
        if self.is_empty():
            print("Stack Underflow")
            return None

        if self.is_static:
            x = self.stack[self.top]
            self.top -= 1
            return x
        else:
            return self.stack.pop()

    def is_empty(self):
        if self.is_static:
            return self.top == -1
        return len(self.stack) == 0

    # ✅ متد تغییر نوع پشته
    def toggle_stack_type(self):
        if self.is_static:
            # استاتیک → داینامیک
            new_stack = []
            for i in range(self.top + 1):
                new_stack.append(self.stack[i])

            self.stack = new_stack
            self.is_static = False
            print("Stack changed to Dynamic")

        else:
            # داینامیک → استاتیک
            new_stack = [None] * self.size
            n = min(len(self.stack), self.size)

            for i in range(n):
                new_stack[i] = self.stack[i]

            self.stack = new_stack
            self.top = n - 1
            self.is_static = True
            print("Stack changed to Static")

    def display(self):
        if self.is_static:
            print(self.stack[:self.top + 1])
        else:
            print(self.stack)







s = Stack(5)

s.push(10)
s.push(20)
s.push(30)

s.toggle_stack_type()  # استاتیک → داینامیک
s.push(40)
s.push(50)
s.push(60)

s.toggle_stack_type()  # داینامیک → استاتیک
s.display()
