class HashTable:
    def __init__(self, size):
        self.size = size
        self.slots = [None] * size
        self.data = [None] * size

    def put(self, key, data):
        hash_value = self.hash(key)

        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        elif self.slots[hash_value] == key:
            self.data[hash_value] = data
        else:
            next_hash_value = self.rehash(hash_value)

            while self.slots[next_hash_value] is not None and self.slots[next_hash_value] != key:
                next_hash_value = self.rehash(next_hash_value)
            if self.slots[next_hash_value] is None:
                self.slots[next_hash_value] = key
                self.data[next_hash_value] = data
            else:
                self.data[next_hash_value] = data

    def hash(self, key):
        return key % self.size

    def rehash(self, old_hash):
        return (old_hash + 1) % self.size

    def get(self, key):
        start_slot = self.hash(key)

        data = None
        stop = False
        found = False
        position = start_slot
        while self.slots[position] is not None and not found and not stop:
            if self.slots[position] == key:
                data = self.data[position]
                found = True
            else:
                position = self.rehash(position)
                if position == start_slot:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)


def main():
    h = HashTable(7)
    h[11] = '一'
    h[21] = '二'
    h[71] = '三'
    h[211] = '四'
    h[271] = '五'
    h[711] = '六'
    print('h\'s slots: ' + str(h.slots))
    print('h\'s data: ' + str(h.data))
    print(h[888])
    print(h[711])
    h[711] = '七'
    print(h[711])
    print('h\'s data: ' + str(h.data))


if __name__ == '__main__':
    main()
