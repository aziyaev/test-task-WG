class CyclesBuffer:
    def __init__(self, size):
        self.items = [0] * size
        self.head_index = 0
        self.tail_index = 0
        self.count = 0
        self.size = size

    def push(self, item):
        if self.is_full():
            raise Exception("Buffer is full")

        self.items[self.head_index] = item
        self.count += 1
        self.head_index = self.move_index(self.head_index)

    def pop(self):
        if self.is_empty():
            raise Exception("Buffer is empty")

        item = self.items[self.tail_index]
        self.count -= 1
        self.tail_index = self.move_index(self.tail_index)

        return item

    def is_full(self):
        return self.count == self.size

    def is_empty(self):
        return self.count == 0

    def move_index(self, index):
        if index + 1 > self.size:
            return 0
        else:
            index += 1
            return index

    def count(self):
        return self.count

    def size(self):
        return self.size
