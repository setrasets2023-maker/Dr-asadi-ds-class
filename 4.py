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
            print("Queue is Full")
            return

        if self.is_empty():
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size

        self.queue[self.rear] = x

    def dequeue(self):
        if self.is_empty():
            print("Queue is Empty")
            return None

        x = self.queue[self.front]

        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

        return x

    # ✅ متد گزارش ۵ لاگ آخر
    def last_five_logs(self):
        if self.is_empty():
            print("No logs available")
            return

        count = self.count_elements()
        logs_to_show = min(5, count)

        result = []
        index = self.rear

        for _ in range(logs_to_show):
            result.append(self.queue[index])
            index = (index - 1 + self.size) % self.size

        result.reverse()  # ترتیب صحیح
        print("Last logs:", result)

    def count_elements(self):
        if self.rear >= self.front:
            return self.rear - self.front + 1
        return self.size - self.front + self.rear + 1





cq = CircularQueue(7)

cq.enqueue("Log1")
cq.enqueue("Log2")
cq.enqueue("Log3")
cq.enqueue("Log4")
cq.enqueue("Log5")
cq.enqueue("Log6")
cq.enqueue("Log7")

cq.last_five_logs()
