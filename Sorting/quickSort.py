def quick_sort(l):
    quick_sort_helper(l, 0, len(l) - 1)


def quick_sort_helper(l, first, last):
    if first < last:
        mid = (last - first) // 2 + first
        sorted_list = sorted([l[first], l[mid], l[last]])
        if mid != first and mid != last:
            l[first], l[first + 1], l[mid], l[last] = sorted_list[0], sorted_list[1], l[first + 1], sorted_list[2]

            split_point = partition(l, first, last)

            quick_sort_helper(l, first, split_point - 1)
            quick_sort_helper(l, split_point + 1, last)
        else:
            l[first], l[last] = sorted_list[0], sorted_list[2]


def partition(l, first, last):
    pivot_value = l[first + 1]

    left_mark = first + 2
    right_mark = last - 1

    done = False

    while not done:
        while left_mark <= right_mark and pivot_value > l[left_mark]:
            left_mark += 1

        while left_mark <= right_mark and pivot_value < l[right_mark]:
            right_mark -= 1

        if left_mark < right_mark:
            l[left_mark], l[right_mark] = l[right_mark], l[left_mark]
        else:
            done = True

    l[first + 1], l[right_mark] = l[right_mark], l[first + 1]

    return right_mark


def main():
    import random
    test_list = [random.randrange(21)]
    quick_sort(test_list)
    print(test_list)


if __name__ == '__main__':
    main()
