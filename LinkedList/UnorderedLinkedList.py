class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next


class UnorderedLinkedList:
    def __init__(self):
        self.head = None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while current and not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if found and not previous:
            self.head = current.get_next()
        elif found:
            previous.set_next(current.get_next())

    def append(self, item):
        temp = Node(item)
        current = self.head
        previous = None
        while current:
            previous = current
            current = current.get_next()

        if not previous:
            self.head = temp
        else:
            previous.set_next(temp)

    def pop(self, pos=None):
        current = self.head
        previous = None
        index = 0
        if not current:
            return

        while current.get_next():
            if pos is not None and index >= pos:
                break
            index += 1
            previous = current
            current = current.get_next()

        if pos and index < pos:
            return

        if not previous:
            self.head = current.get_next() if pos is not None else None
            return current.get_data()
        else:
            previous.set_next(current.get_next() if pos is not None else None)
            return current.get_data()

    def insert(self, pos, item):
        temp = Node(item)
        current = self.head
        previous = None
        index = 0
        while current and index < pos:
            index += 1
            previous = current
            current = current.get_next()

        if not previous:
            temp.set_next(current)
            self.head = temp
        else:
            temp.set_next(current)
            previous.set_next(temp)

    def search(self, item):
        current = self.head
        found = False
        while current and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()

        return found

    def index(self, item):
        current = self.head
        found = False
        index = 0
        while current and not found:
            if current.get_data() == item:
                found = True
            else:
                index += 1
                current = current.get_next()

        if found:
            return index
        else:
            return None

    def is_empty(self):
        return self.head is None

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()

        return count


def show(linked_list):
    current = linked_list.head

    data = []
    while current:
        data.append(current.get_data())
        current = current.get_next()

    return ', '.join([str(d) for d in data])
