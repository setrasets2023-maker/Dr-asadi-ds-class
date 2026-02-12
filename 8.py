class CircularQueue:
    def __init__(self, size=10):
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

    # ✅ متد تبدیل صف حلقوی به صف ساده
    def to_simple_queue(self):
        if self.is_empty():
            return

        new_queue = [None] * self.size
        i = self.front
        idx = 0

        while True:
            new_queue[idx] = self.queue[i]
            if i == self.rear:
                break
            i = (i + 1) % self.size
            idx += 1

        self.queue = new_queue
        self.front = 0
        self.rear = idx
