class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0 or None

    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)
        else:
            print("Stack is full")

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) == self.limit

    def search(self, target):
        for i in range(len(self.items) -1, -1, -1):
            if self.items[i] == target:
                return len(self.items) - 1 - i
        else:
            return -1
