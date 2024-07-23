class Stack:
    
    def __init__(self, items=None, limit=100):
        self.items = items if items is not None else []
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)
        else:
            print("Stack is full!")

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            print("Stack is empty!")
            return None

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            print("Stack is empty!")
            return None

    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) == self.limit

    def search(self, target):
        if target in self.items:
        # Calculate the index from the top
            index_from_top = len(self.items) - self.items.index(target)
            return index_from_top
        else:
            return -1

