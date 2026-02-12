from datetime import datetime

class CircularQueue:
    def __init__(self, size=5):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

        # ذخیره ۵ زمان آخر پر شدن صف
        self.full_times = []

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def is_empty(self):
        return self.front == -1

    def enqueue(self, x):
        if self.is_full():
            self._save_full_time()
            return

        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size

        self.queue[self.rear] = x

    # ✅ ثبت زمان پر شدن صف
    def _save_full_time(self):
        time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.full_times.append(time_now)

        if len(self.full_times) > 5:
            self.full_times.pop(0)

    # ✅ متد گزارش ۵ زمان آخر پر شدن صف
    def report_full_times(self):
        if not self.full_times:
            print("Queue has never been full")
            return

        for t in self.full_times:
            print(t)








