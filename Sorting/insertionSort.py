def insertion_sort(l):
    for index in range(1, len(l)):
        current_value = l[index]
        position = index

        while position > 0 and current_value < l[position - 1]:
            l[position] = l[position - 1]
            position -= 1

        l[position] = current_value


def main():
    test_list = [211, 21, 71, 711, 11]
    insertion_sort(test_list)
    print(test_list)


if __name__ == '__main__':
    main()
