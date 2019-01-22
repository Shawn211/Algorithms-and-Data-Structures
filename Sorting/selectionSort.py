def selection_sort(l):
    for comparison_number in range(len(l) - 1, 0, -1):
        position = 0
        for i in range(comparison_number + 1):
            if l[i] > l[position]:
                position = i

        l[position], l[comparison_number] = l[comparison_number], l[position]


def main():
    test_list = [211, 21, 71, 711, 11]
    selection_sort(test_list)
    print(test_list)


if __name__ == '__main__':
    main()
