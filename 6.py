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

    def get_valid_elements(self):
        if self.is_empty():
            return []

        result = []
        i = self.front
        while True:
            result.append(self.queue[i])
            if i == self.rear:
                break
            i = (i + 1) % self.size
        return result







def create_and_transfer():
    queues = []
    stacks = []

    # ایجاد ۱۰۰۰ صف حلقوی
    for i in range(1000):
        q = CircularQueue()
        for j in range(3):       # داده نمونه
            q.enqueue(i * 10 + j)
        queues.append(q)

    # ایجاد ۱۰۰۰ پشته
    for _ in range(1000):
        stacks.append(Stack())

    # انتقال داده‌های معتبر صف‌ها به‌صورت معکوس به پشته‌ها
    for i in range(1000):
        data = queues[i].get_valid_elements()
        for x in reversed(data):
            stacks[i].push(x)

    return queues, stacks
