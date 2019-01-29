class MinHeap:
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def insert(self, value):
        self.heap_list.append(value)
        self.current_size += 1
        self.percolate_up(self.current_size)

    def percolate_up(self, i):
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i // 2]:
                self.heap_list[i], self.heap_list[i // 2] = self.heap_list[i // 2], self.heap_list[i]
            i //= 2

    def del_min(self):
        return_value = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size -= 1
        self.heap_list.pop()
        self.percolate_down(1)
        return return_value

    def percolate_down(self, i):
        while i * 2 <= self.current_size:
            min_child = self.min_child(i)
            if self.heap_list[i] > self.heap_list[min_child]:
                self.heap_list[i], self.heap_list[min_child] = self.heap_list[min_child], self.heap_list[i]
            i = min_child

    def min_child(self, i):
        if i * 2 + 1 > self.current_size:
            return i * 2
        else:
            if self.heap_list[i * 2] < self.heap_list[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def build_heap(self, l):
        i = len(l) // 2
        self.current_size = len(l)
        self.heap_list = [0] + l[:]
        while i > 0:
            self.percolate_down(i)
            i -= 1

    def find_min(self):
        return self.heap_list[1]

    def is_empty(self):
        return self.current_size == 0

    def size(self):
        return self.current_size


def main():
    heap = MinHeap()
    heap.build_heap([211, 21, 71, 711, 11])

    print(heap.find_min())
    print(heap.size())
    print(heap.del_min())
    print(heap.del_min())
    print(heap.del_min())
    print(heap.del_min())
    print(heap.del_min())
    print(heap.is_empty())


if __name__ == '__main__':
    main()
