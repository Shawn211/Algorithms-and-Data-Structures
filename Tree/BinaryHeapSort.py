from MinHeap import MinHeap
from MaxHeap import MaxHeap


def min_heap_sort(l):
    heap = MinHeap()
    heap.build_heap(l)
    i = 0
    while heap.current_size > 0:
        l[i] = heap.del_min()
        i += 1


def max_heap_sort(l):
    heap = MaxHeap()
    heap.build_heap(l)
    i = 0
    while heap.current_size > 0:
        l[i] = heap.del_max()
        i += 1


def main():
    test_list = [211, 21, 71, 711, 11]
    min_heap_sort(test_list)
    print(test_list)
    test_list = [211, 21, 71, 711, 11]
    max_heap_sort(test_list)
    print(test_list)


if __name__ == '__main__':
    main()
