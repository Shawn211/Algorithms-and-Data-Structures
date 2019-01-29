def binary_tree(r):
    return [r, [], []]


def insert_left(root, new_node):
    b = root.pop(1)
    if len(b) > 1:
        root.insert(1, [new_node, b, []])
    else:
        root.insert(1, [new_node, [], []])
    return root


def insert_right(root, new_node):
    b = root.pop(2)
    if len(b) > 1:
        root.insert(2, [new_node, [], b])
    else:
        root.insert(2, [new_node, [], []])
    return root


def get_root_value(root):
    return root[0]


def set_root_value(root, new_value):
    root[0] = new_value


def get_left_child(root):
    return root[1]


def get_right_child(root):
    return root[2]


def main():
    tree = binary_tree(21)
    print(tree)
    insert_left(tree, 11)
    insert_right(tree, 71)
    print(tree)
    insert_right(tree, 711)
    set_root_value(tree, 211)
    print(get_root_value(tree))
    print(get_left_child(tree))
    print(get_right_child(tree))


if __name__ == '__main__':
    main()
