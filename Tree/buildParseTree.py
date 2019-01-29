import operator
from Stack import Stack
from BinaryTree import BinaryTree


def build_parse_tree(fully_parenthesized_expressions):
    fplist = fully_parenthesized_expressions.split()

    p_stack = Stack()
    tree = BinaryTree('')

    p_stack.push(tree)
    current_tree = tree

    for i in fplist:
        if i == '(':
            current_tree.insert_left('')
            p_stack.push(current_tree)
            current_tree = current_tree.get_left_child()
        elif i not in ['+', '-', '/', '*', ')']:
            current_tree.set_root_value(int(i))
            current_tree = p_stack.pop()
        elif i in ['+', '-', '/', '*']:
            current_tree.set_root_value(i)
            current_tree.insert_right('')
            p_stack.push(current_tree)
            current_tree = current_tree.get_right_child()
        elif i == ')':
            current_tree = p_stack.pop()
        else:
            raise ValueError
    return tree


def evaluate(parse_tree):
    operators = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}

    left_child = parse_tree.get_left_child()
    right_child = parse_tree.get_right_child()

    if left_child and right_child:
        return operators[parse_tree.get_root_value()](evaluate(left_child), evaluate(right_child))
    else:
        return parse_tree.get_root_value()


def main():
    tree = build_parse_tree('( ( 11 + 6 ) * 2 )')
    print(evaluate(tree))


if __name__ == '__main__':
    main()
