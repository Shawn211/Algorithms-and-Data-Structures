from buildParseTree import build_parse_tree


def pre_order(tree):
    if tree:
        print(tree.get_root_value())
        pre_order(tree.get_left_child())
        pre_order(tree.get_right_child())


def post_order(tree):
    if tree:
        post_order(tree.get_left_child())
        post_order(tree.get_right_child())
        print(tree.get_root_value())


def in_order(tree):
    if tree:
        in_order(tree.get_left_child())
        print(tree.get_root_value())
        in_order(tree.get_right_child())


def print_expressions(tree):
    exp = ''
    if tree:
        exp = '(' + print_expressions(tree.get_left_child())
        exp += str(tree.get_root_value())
        exp = exp + print_expressions(tree.get_right_child()) + ')'
    return exp


def main():
    tree = build_parse_tree('( ( 11 + 6 ) * 2 )')
    print('前序遍历:')
    pre_order(tree)
    print('后序遍历:')
    post_order(tree)
    print('中序遍历:')
    in_order(tree)
    print('表达式:', print_expressions(tree))


if __name__ == '__main__':
    main()
