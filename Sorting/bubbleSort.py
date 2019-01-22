def bubble_sort(l):
    exchanges = True
    for comparison_number in range(len(l) - 1, 0, -1):
        if not exchanges:
            break
        exchanges = False
        for i in range(comparison_number):
            if l[i] > l[i + 1]:
                exchanges = True
                l[i], l[i + 1] = l[i + 1], l[i]


def main():
    test_list = [211, 21, 71, 711, 11]
    bubble_sort(test_list)
    print(test_list)


if __name__ == '__main__':
    main()
