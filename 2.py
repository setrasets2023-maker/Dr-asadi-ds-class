class Stack:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        if self.is_empty():
            print("Stack Underflow")
            return None
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        print(self.items)

    # ✅ متد اولویت‌بندی زوج و فرد
    def prioritize_even_odd(self):
        even = []
        odd = []

        # تخلیه پشته
        while not self.is_empty():
            x = self.pop()
            if x % 2 == 0:
                even.append(x)
            else:
                odd.append(x)

        # بازگرداندن: اول زوج‌ها، بعد فردها
        for x in reversed(odd):
            self.push(x)

        for x in reversed(even):
            self.push(x)






s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)

s.prioritize_even_odd()
s.display()
