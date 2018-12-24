def binary_search(l, item):
    if len(l) == 0:
        return False
    else:
        midpoint = len(l) // 2
        if l[midpoint] == item:
            return True
        elif l[midpoint] < item:
            return binary_search(l[midpoint + 1:], item)
        else:
            return binary_search(l[:midpoint], item)


def main():
    test_list = [11, 21, 71, 211, 711]
    print(binary_search(test_list, 71))


if __name__ == '__main__':
    main()
