class AdvancedStack:
    # 1
    def __init__(self):
        self.stack = []

    # 2
    def is_empty(self):
        return len(self.stack) == 0

    # 3
    def size(self):
        return len(self.stack)

    # 4
    def push(self, x):
        self.stack.append(x)

    # 5
    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    # 6
    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    # 7
    def clear(self):
        self.stack.clear()

    # 8
    def contains(self, x):
        return x in self.stack

    # 9
    def reverse(self):
        self.stack.reverse()

    # 10
    def copy(self):
        return self.stack.copy()

    # 11
    def get_min(self):
        return min(self.stack) if not self.is_empty() else None

    # 12
    def get_max(self):
        return max(self.stack) if not self.is_empty() else None

    # 13
    def sum(self):
        return sum(self.stack)

    # 14
    def average(self):
        if self.is_empty():
            return None
        return sum(self.stack) / self.size()

    # 15
    def count_even(self):
        return sum(1 for x in self.stack if x % 2 == 0)

    # 16
    def count_odd(self):
        return sum(1 for x in self.stack if x % 2 != 0)

    # 17
    def remove_duplicates(self):
        self.stack = list(dict.fromkeys(self.stack))

    # 18
    def sort_ascending(self):
        self.stack.sort()

    # 19
    def sort_descending(self):
        self.stack.sort(reverse=True)

    # 20
    def prioritize(self):
        self.sort_descending()

    # 21
    def push_multiple(self, items):
        for x in items:
            self.push(x)

    # 22
    def pop_multiple(self, k):
        result = []
        for _ in range(min(k, self.size())):
            result.append(self.pop())
        return result

    # 23
    def is_palindrome(self):
        return self.stack == self.stack[::-1]

    # 24
    def get_middle(self):
        if self.is_empty():
            return None
        return self.stack[self.size() // 2]

    # 25
    def replace(self, old, new):
        self.stack = [new if x == old else x for x in self.stack]

    # 26
    def remove_value(self, x):
        self.stack = [v for v in self.stack if v != x]

    # 27
    def frequency(self, x):
        return self.stack.count(x)

    # 28
    def max_frequency(self):
        if self.is_empty():
            return None
        return max(set(self.stack), key=self.stack.count)

    # 29
    def min_frequency(self):
        if self.is_empty():
            return None
        return min(set(self.stack), key=self.stack.count)

    # 30
    def push_if_unique(self, x):
        if x not in self.stack:
            self.push(x)

    # 31
    def swap_top(self):
        if self.size() < 2:
            return
        self.stack[-1], self.stack[-2] = self.stack[-2], self.stack[-1]

    # 32
    def rotate_left(self):
        if self.size() > 1:
            self.stack.append(self.stack.pop(0))

    # 33
    def rotate_right(self):
        if self.size() > 1:
            self.stack.insert(0, self.stack.pop())

    # 34
    def to_string(self):
        return " ".join(map(str, self.stack))

    # 35
    def info(self):
        return {
            "size": self.size(),
            "is_empty": self.is_empty(),
            "top": self.peek()
        }
