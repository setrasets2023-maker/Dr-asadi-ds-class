# ===============================
# Circular Queue (صف حلقوی)
# ===============================
class CircularQueue:
    def __init__(self, size=5):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def enqueue(self, x):
        if self.is_full():
            return
        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = x

    def dequeue(self):
        if self.is_empty():
            return None
        value = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return value


# ===============================
# Stack (پشته)
# ===============================
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

    def peek(self):
        return None if self.is_empty() else self.stack[-1]


# ===============================
# Hybrid Structure
# (ارث‌بری از صف حلقوی و پشته)
# ===============================
class HybridStructure(CircularQueue, Stack):
    def __init__(self, size=5):
        super().__init__(size)   # سازنده CircularQueue
        self.stack = []          # سازنده Stack

    # اضافه کردن داده (رفتار صف)
    def add(self, x):
        self.enqueue(x)

    # انتقال عناصر صف به پشته
    def queue_to_stack(self):
        if self.is_empty():
            return

        i = self.front
        while True:
            self.stack.append(self.queue[i])
            if i == self.rear:
                break
            i = (i + 1) % self.size

    # حذف با اولویت پشته
    def remove(self):
        if self.stack:
            return self.stack.pop()
        return self.dequeue()

    # وضعیت ساختار
    def status(self):
        return {
            "queue": self.queue,
            "front": self.front,
            "rear": self.rear,
            "stack": self.stack
        }

    # پاک‌سازی کامل
    def clear_all(self):
        self.front = self.rear = -1
        self.queue = [None] * self.size
        self.stack.clear()
