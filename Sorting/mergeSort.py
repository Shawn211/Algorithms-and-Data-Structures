def merge_sort(l):
    first = 0
    last = len(l)
    temp_list = l[:]
    merge_sort_helper(l, first, last, temp_list)


def merge_sort_helper(l, first, last, temp_list):
    if first is None:
        first = 0
        temp_list = l[:]
    if last is None:
        last = len(l)
        temp_list = l[:]

    if last - first > 1:
        mid = (last - first) // 2 + first

        merge_sort_helper(l, first, mid, temp_list)
        merge_sort_helper(l, mid, last, temp_list)

        i = 0
        j = 0
        k = first
        while i < mid - first and j < last - mid:
            if temp_list[first + i] < temp_list[mid + j]:
                l[k] = temp_list[first + i]
                i += 1
            else:
                l[k] = temp_list[mid + j]
                j += 1
            k += 1

        while i < mid - first:
            l[k] = temp_list[first + i]
            i += 1
            k += 1
        while j < last - mid:
            l[k] = temp_list[mid + j]
            j += 1
            k += 1
        temp_list[:] = l[:]


def main():
    test_list = [211, 21, 71, 711, 11]
    merge_sort(test_list)
    print(test_list)


if __name__ == '__main__':
    main()
