class ListItem:
    def __init__(self, next_el = None):
        self.data = 0
        self.next_el = next_el

    def next_el(self):
        return self.next_el

    def set_next_el(self, el):
        self.next_el = el

    def data(self):
        return self.data

    def set_data(self, data):
        self.data = data

class CyclesBufferList:
    def __init__(self, size):
        self.size = size
        self.count = 0

        item = ListItem()
        first_item = item

        for i in range(size - 1):
            item = ListItem(item)

        first_item.set_next_el(item)
        self.head_el = first_item
        self.tail_el = first_item

    def size(self):
        return self.size

    def count(self):
        return self.count

    def isListEmpty(self):
        return self.count == 0

    def isListFull(self):
        return self.count == self.size

    def push(self, el):
        if self.isListFull():
            raise Exception("Buffer is full")

        self.head_el.set_data(el)
        self.head_el = self.head_el.next_el()
        self.count += 1

    def pop(self):
        if self.isListEmpty():
            raise Exception("Buffer is empty")

        item = self.tail_el.data()
        self.tail_el = self.tail_el.next_el()
        self.count -= 1

        return item




