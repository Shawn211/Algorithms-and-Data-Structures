def shell_sort(l):
    sublist_count = len(l) // 2

    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(l, start_position, sublist_count)

        sublist_count //= 2


def gap_insertion_sort(l, start, gap):
    for i in range(start+gap, len(l), gap):
        current_value = l[i]
        position = i

        while position > 0 and current_value < l[position - gap]:
            l[position] = l[position - gap]
            position -= gap

        l[position] = current_value


def main():
    test_list = [211, 21, 71, 711, 11]
    shell_sort(test_list)
    print(test_list)


if __name__ == '__main__':
    main()
