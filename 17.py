# ======================================
# Node (گره چهار بعدی)
# ======================================
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        self.down = None
        self.up = None


# ======================================
# Four Dimensional Linked List
# ======================================
class FourDimensionalLinkedList:
    def __init__(self):
        self.head = None


    # 1
    def is_empty(self):
        return self.head is None


    # 2
    def add_first(self, data):
        new_node = Node(data)
        if not self.is_empty():
            self.head.prev = new_node
            new_node.next = self.head
        self.head = new_node


    # 3
    def add_last(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp


    # 4
    def remove_first(self):
        if self.is_empty():
            return None
        value = self.head.data
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        return value


    # 5
    def remove_last(self):
        if self.is_empty():
            return None
        temp = self.head
        while temp.next:
            temp = temp.next
        if temp.prev:
            temp.prev.next = None
        else:
            self.head = None
        return temp.data


    # 6
    def search(self, data):
        temp = self.head
        while temp:
            if temp.data == data:
                return True
            temp = temp.next
        return False


    # 7
    def count(self):
        cnt = 0
        temp = self.head
        while temp:
            cnt += 1
            temp = temp.next
        return cnt


    # 8
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")


    # 9
    def add_down(self, parent_data, child_data):
        temp = self.head
        while temp:
            if temp.data == parent_data:
                temp.down = Node(child_data)
                return
            temp = temp.next


    # 10
    def add_up(self, parent_data, child_data):
        temp = self.head
        while temp:
            if temp.data == parent_data:
                temp.up = Node(child_data)
                return
            temp = temp.next


    # 11
    def remove_down(self, data):
        temp = self.head
        while temp:
            if temp.data == data:
                temp.down = None
                return
            temp = temp.next


    # 12
    def remove_up(self, data):
        temp = self.head
        while temp:
            if temp.data == data:
                temp.up = None
                return
            temp = temp.next


    # 13
    def has_down(self, data):
        temp = self.head
        while temp:
            if temp.data == data:
                return temp.down is not None
            temp = temp.next
        return False


    # 14
    def has_up(self, data):
        temp = self.head
        while temp:
            if temp.data == data:
                return temp.up is not None
            temp = temp.next
        return False


    # 15
    def clear(self):
        self.head = None
