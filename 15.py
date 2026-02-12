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


# ===============================
# Postfix to Infix
# ===============================
def postfix_to_infix(expression):
    stack = Stack()
    operators = {'+', '-', '*', '/', '^'}

    for ch in expression:
        # اگر عملوند بود
        if ch not in operators:
            stack.push(ch)
        else:
            # اگر عملگر بود
            op2 = stack.pop()
            op1 = stack.pop()
            new_expr = "(" + op1 + ch + op2 + ")"
            stack.push(new_expr)

    return stack.pop()






exp = "ab+c*"
print(postfix_to_infix(exp))
