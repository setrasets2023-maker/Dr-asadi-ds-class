class MegaStack:

    # ===== متدهای پایه (1–10) =====
    def __init__(self):                       # 1
        self.stack = []

    def is_empty(self):                       # 2
        return len(self.stack) == 0

    def size(self):                           # 3
        return len(self.stack)

    def push(self, x):                        # 4
        self.stack.append(x)

    def pop(self):                            # 5
        if self.is_empty():
            return None
        return self.stack.pop()

    def peek(self):                           # 6
        return None if self.is_empty() else self.stack[-1]

    def clear(self):                          # 7
        self.stack.clear()

    def copy(self):                           # 8
        return self.stack.copy()

    def to_list(self):                        # 9
        return list(self.stack)

    def contains(self, x):                    # 10
        return x in self.stack

    # ===== آماری (11–20) =====
    def get_min(self):                        # 11
        return min(self.stack) if not self.is_empty() else None

    def get_max(self):                        # 12
        return max(self.stack) if not self.is_empty() else None

    def get_sum(self):                        # 13
        return sum(self.stack)

    def average(self):                        # 14
        return self.get_sum() / self.size() if not self.is_empty() else None

    def count_even(self):                     # 15
        return sum(1 for x in self.stack if x % 2 == 0)

    def count_odd(self):                      # 16
        return sum(1 for x in self.stack if x % 2 != 0)

    def frequency(self, x):                   # 17
        return self.stack.count(x)

    def max_frequency(self):                  # 18
        return max(set(self.stack), key=self.stack.count) if self.stack else None

    def min_frequency(self):                  # 19
        return min(set(self.stack), key=self.stack.count) if self.stack else None

    def unique_count(self):                   # 20
        return len(set(self.stack))

    # ===== مرتب‌سازی و اولویت (21–30) =====
    def sort_ascending(self):                 # 21
        self.stack.sort()

    def sort_descending(self):                # 22
        self.stack.sort(reverse=True)

    def prioritize(self):                     # 23
        self.sort_descending()

    def remove_duplicates(self):              # 24
        self.stack = list(dict.fromkeys(self.stack))

    def push_if_unique(self, x):               # 25
        if x not in self.stack:
            self.push(x)

    def replace(self, old, new):               # 26
        self.stack = [new if x == old else x for x in self.stack]

    def remove_value(self, x):                 # 27
        self.stack = [v for v in self.stack if v != x]

    def get_middle(self):                      # 28
        return self.stack[self.size() // 2] if not self.is_empty() else None

    def is_sorted(self):                       # 29
        return self.stack == sorted(self.stack)

    def reverse(self):                         # 30
        self.stack.reverse()

    # ===== چندعملیاتی (31–40) =====
    def push_multiple(self, items):            # 31
        for x in items:
            self.push(x)

    def pop_multiple(self, k):                 # 32
        result = []
        for _ in range(min(k, self.size())):
            result.append(self.pop())
        return result

    def swap_top(self):                        # 33
        if self.size() >= 2:
            self.stack[-1], self.stack[-2] = self.stack[-2], self.stack[-1]

    def rotate_left(self):                     # 34
        if self.size() > 1:
            self.stack.append(self.stack.pop(0))

    def rotate_right(self):                    # 35
        if self.size() > 1:
            self.stack.insert(0, self.stack.pop())

    def duplicate_top(self):                   # 36
        if not self.is_empty():
            self.push(self.peek())

    def remove_top(self):                      # 37
        if not self.is_empty():
            self.pop()

    def bottom(self):                          # 38
        return self.stack[0] if not self.is_empty() else None

    def remove_bottom(self):                   # 39
        if not self.is_empty():
            self.stack.pop(0)

    def insert_bottom(self, x):                # 40
        self.stack.insert(0, x)

    # ===== منطقی و الگوریتمی (41–55) =====
    def is_palindrome(self):                   # 41
        return self.stack == self.stack[::-1]

    def all_positive(self):                    # 42
        return all(x > 0 for x in self.stack)

    def any_negative(self):                    # 43
        return any(x < 0 for x in self.stack)

    def find_index(self, x):                   # 44
        return self.stack.index(x) if x in self.stack else -1

    def count_greater_than(self, k):           # 45
        return sum(1 for x in self.stack if x > k)

    def count_less_than(self, k):              # 46
        return sum(1 for x in self.stack if x < k)

    def map_square(self):                      # 47
        self.stack = [x * x for x in self.stack]

    def filter_even(self):                     # 48
        self.stack = [x for x in self.stack if x % 2 == 0]

    def filter_odd(self):                      # 49
        self.stack = [x for x in self.stack if x % 2 != 0]

    def sum_top_k(self, k):                    # 50
        return sum(self.stack[-k:])

    def compare_size(self, other):             # 51
        return self.size() - other.size()

    def merge(self, other):                    # 52
        self.push_multiple(other.to_list())

    def equals(self, other):                   # 53
        return self.stack == other.to_list()

    def clear_if_full(self, limit):             # 54
        if self.size() >= limit:
            self.clear()

    def trim(self, k):                         # 55
        self.stack = self.stack[:k]

    # ===== نمایشی و اطلاعاتی (56–65) =====
    def to_string(self):                       # 56
        return " ".join(map(str, self.stack))

    def print_stack(self):                     # 57
        print(self.stack)

    def info(self):                            # 58
        return {
            "size": self.size(),
            "is_empty": self.is_empty(),
            "top": self.peek()
        }

    def memory_usage(self):                    # 59
        return self.size() * 8   # تخمینی

    def reset(self):                           # 60
        self.clear()

    def clone(self):                           # 61
        new = MegaStack()
        new.push_multiple(self.stack)
        return new

    def push_range(self, a, b):                # 62
        for i in range(a, b + 1):
            self.push(i)

    def remove_range(self, a, b):              # 63
        self.stack = [x for x in self.stack if not (a <= x <= b)]

    def count_range(self, a, b):               # 64
        return sum(1 for x in self.stack if a <= x <= b)

    def checksum(self):                        # 65
        return hash(tuple(self.stack))
