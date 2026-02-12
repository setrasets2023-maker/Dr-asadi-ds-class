# ===============================
# Stack (پشته)
# ===============================
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, x):
        self.items.append(x)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        return None if self.is_empty() else self.items[-1]


# ===============================
# Queue using Stack (صف با پشته)
# ===============================
class QueueWithStack:
    def __init__(self):
        self.stack1 = Stack()  # برای enqueue
        self.stack2 = Stack()  # برای dequeue

    # اضافه کردن عنصر (enqueue)
    def enqueue(self, x):
        self.stack1.push(x)

    # حذف عنصر (dequeue)
    def dequeue(self):
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())

        return self.stack2.pop()

    # مشاهده عنصر جلویی صف
    def front(self):
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())

        return self.stack2.peek()

    # بررسی خالی بودن صف
    def is_empty(self):
        return self.stack1.is_empty() and self.stack2.is_empty()
