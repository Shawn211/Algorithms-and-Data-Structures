def sequential_search(l, item):
    pos = 0
    found = False

    while pos < len(l) and not found:
        if l[pos] == item:
            found = True
        else:
            pos += 1

    return found


def main():
    test_list = [211, 21, 71, 711, 11]
    print(sequential_search(test_list, 11))


if __name__ == '__main__':
    main()
