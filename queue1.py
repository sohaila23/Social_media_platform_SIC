class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return None if self.isEmpty() else self.items.pop(0)

    def size(self):
        return len(self.items)

    def peek(self):
        return None if self.isEmpty() else self.items[ : :-1]