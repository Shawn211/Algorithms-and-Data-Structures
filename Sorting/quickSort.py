def quick_sort(l):
    quick_sort_helper(l, 0, len(l) - 1)


def quick_sort_helper(l, first, last):
    if first < last:
        split_point = partition(l, first, last)

        quick_sort_helper(l, first, split_point - 1)
        quick_sort_helper(l, split_point + 1, last)


def partition(l, first, last):
    pivot_value = l[first]

    left_mark = first + 1
    right_mark = last

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

    l[first], l[right_mark] = l[right_mark], l[first]

    return right_mark


def main():
    test_list = [211, 21, 71, 711, 11]
    quick_sort(test_list)
    print(test_list)


if __name__ == '__main__':
    main()
