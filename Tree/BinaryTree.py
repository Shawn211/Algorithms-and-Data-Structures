class BinaryTree:
    def __init__(self, root_obj):
        self.key = root_obj
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        if not self.left_child:
            self.left_child = BinaryTree(new_node)
        else:
            n = BinaryTree(new_node)
            n.left_child = self.left_child
            self.left_child = n

    def insert_right(self, new_node):
        if not self.right_child:
            self.right_child = BinaryTree(new_node)
        else:
            n = BinaryTree(new_node)
            n.right_child = self.right_child
            self.right_child = n

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def set_root_value(self, new_value):
        self.key = new_value

    def get_root_value(self):
        return self.key


def main():
    tree = BinaryTree('a')
    print(tree.get_root_value())
    print(tree.get_left_child())
    tree.insert_left('b')
    print(tree.get_left_child())
    print(tree.get_left_child().get_root_value())
    tree.insert_right('c')
    print(tree.get_right_child())
    print(tree.get_right_child().get_root_value())
    tree.get_right_child().set_root_value('hello')
    print(tree.get_right_child().get_root_value())


if __name__ == '__main__':
    main()
