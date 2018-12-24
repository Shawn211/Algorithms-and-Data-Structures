def ordered_sequential_search(l, item):
    pos = 0
    found = False
    stop = False

    while pos < len(l) and not found and not stop:
        if l[pos] == item:
            found = True
        elif l[pos] > item:
            stop = True
        else:
            pos += 1

    return found


def main():
    test_list = [11, 21, 71, 211, 711]
    print(ordered_sequential_search(test_list, 271))


if __name__ == '__main__':
    main()
