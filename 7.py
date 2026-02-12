# ---------- Circular Queue ----------
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
            return False
        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = x
        return True

    def dequeue(self):
        if self.is_empty():
            return None
        value = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return value


# ---------- Stack ----------
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if not self.stack:
            return None
        return self.stack.pop()

    def stack_empty(self):
        return len(self.stack) == 0


# ---------- Priority Circular Queue ----------
class PriorityCircularQueue(CircularQueue, Stack):

    def __init__(self, size=10):
        CircularQueue.__init__(self, size)
        Stack.__init__(self)

    # 1
    def enqueue_with_priority(self, x):
        if self.is_full():
            return False
        data = self.get_elements()
        data.append(x)
        data.sort(reverse=True)
        self.clear()
        for item in data:
            self.enqueue(item)
        return True

    # 2
    def dequeue_priority(self):
        return self.dequeue()

    # 3
    def peek(self):
        if self.is_empty():
            return None
        return self.queue[self.front]

    # 4
    def get_elements(self):
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

    # 5
    def clear(self):
        self.front = self.rear = -1
        self.queue = [None] * self.size

    # 6
    def count(self):
        return len(self.get_elements())

    # 7
    def contains(self, x):
        return x in self.get_elements()

    # 8
    def reverse(self):
        for x in self.get_elements():
            self.push(x)
        self.clear()
        while not self.stack_empty():
            self.enqueue(self.pop())

    # 9
    def move_to_stack(self):
        for x in self.get_elements():
            self.push(x)

    # 10
    def display(self):
        print(self.get_elements())
