class AVLTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def put(self, key, value):
        if self.root:
            self._put(key, value, self.root)
        else:
            self.root = TreeNode(key, value)
        self.size += 1

    def _put(self, key, value, current_node):
        if key < current_node.key:
            if current_node.has_left_child():
                self._put(key, value, current_node.left_child)
            else:
                current_node.left_child = TreeNode(key, value, parent=current_node)
                self.update_balance(current_node.left_child)
        elif key == current_node.key:
            current_node.value = value
            self.size -= 1
        else:
            if current_node.has_right_child():
                self._put(key, value, current_node.right_child)
            else:
                current_node.right_child = TreeNode(key, value, parent=current_node)
                self.update_balance(current_node.right_child)

    def update_balance(self, node):
        if node.balance_factor > 1 or node.balance_factor < -1:
            self.re_balance(node)
        elif node.parent is not None:
            if node.is_left_child():
                node.parent.balance_factor += 1
            elif node.is_right_child():
                node.parent.balance_factor -= 1
            if node.parent.balance_factor != 0:
                self.update_balance(node.parent)

    def re_balance(self, node):
        if node.balance_factor < 0:
            if node.right_child.balance_factor > 0:
                self.rotate_right(node.right_child)
                self.rotate_left(node)
            else:
                self.rotate_left(node)
        elif node.balance_factor > 0:
            if node.left_child.balance_factor < 0:
                self.rotate_left(node.left_child)
                self.rotate_right(node)
            else:
                self.rotate_right(node)

    def rotate_left(self, node):
        new_root = node.right_child
        node.right_child = new_root.left_child
        if new_root.left_child:
            new_root.left_child.parent = node
        new_root.parent = node.parent
        if node.is_root():
            self.root = new_root
        else:
            if node.is_left_child():
                node.parent.left_child = new_root
            else:
                node.parent.right_child = new_root
        new_root.left_child = node
        node.parent = new_root
        node.balance_factor = node.balance_factor + 1 - min(new_root.balance_factor, 0)
        new_root.balance_factor = new_root.balance_factor + 1 + max(node.balance_factor, 0)

    def rotate_right(self, node):
        new_root = node.left_child
        node.left_child = new_root.right_child
        if new_root.right_child:
            new_root.right_child.parent = node
        new_root.parent = node.parent
        if node.is_root():
            self.root = new_root
        else:
            if node.is_left_child():
                node.parent.left_child = new_root
            else:
                node.parent.right_child = new_root
        new_root.right_child = node
        node.parent = new_root
        node.balance_factor = node.balance_factor - 1 - max(new_root.balance_factor, 0)
        new_root.balance_factor = new_root.balance_factor - 1 + min(node.balance_factor, 0)

    def __setitem__(self, key, value):
        self.put(key, value)

    def get(self, key):
        res = self._get(key, self.root)
        if res:
            return res.value
        else:
            return None

    def _get(self, key, current_node):
        if not current_node:
            return None
        elif current_node.key == key:
            return current_node
        elif current_node.key > key:
            return self._get(key, current_node.left_child)
        else:
            return self._get(key, current_node.right_child)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self.get(key):
            return True
        else:
            return False

    def delete(self, key):
        if self.size > 1:
            node_to_remove = self._get(key, self.root)
            if node_to_remove:
                self.remove(node_to_remove)
                self.size -= 1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        else:
            raise KeyError('Error, key not in tree')

    def remove(self, current_node):
        if current_node.is_leaf():
            if current_node.is_left_child():
                current_node.parent.left_child = None
                self.update_deletion_balance(current_node, left=True)
            else:
                current_node.parent.right_child = None
                self.update_deletion_balance(current_node, left=False)
        elif current_node.has_both_child():
            successor = current_node.find_successor()
            if successor.is_left_child():
                self.update_deletion_balance(successor, left=True)
            else:
                self.update_deletion_balance(successor, left=False)
            successor.splice_out()
            current_node.key = successor.key
            current_node.value = successor.value
        else:
            if current_node.has_left_child():
                if current_node.is_left_child():
                    current_node.left_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.left_child
                    self.update_deletion_balance(current_node, left=True)
                elif current_node.is_right_child():
                    current_node.left_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.left_child
                    self.update_deletion_balance(current_node, left=False)
                else:
                    current_node.replace_node_data(
                        current_node.left_child.key,
                        current_node.left_child.value,
                        current_node.left_child.left_child,
                        current_node.left_child.right_child
                    )
            else:
                if current_node.is_left_child():
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.right_child
                    self.update_deletion_balance(current_node, left=True)
                elif current_node.is_right_child():
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.right_child
                    self.update_deletion_balance(current_node, left=False)
                else:
                    current_node.replace_node_data(
                        current_node.right_child.key,
                        current_node.right_child.value,
                        current_node.right_child.left_child,
                        current_node.right_child.right_child
                    )

    def update_deletion_balance(self, node, left):
        if node.parent is not None:
            if left:
                node.parent.balance_factor -= 1
            else:
                node.parent.balance_factor += 1
            if node.parent.balance_factor != 0:
                if node.parent.balance_factor > 1 or node.parent.balance_factor < -1:
                    self.re_balance(node.parent)
                elif node.parent.parent is not None:
                    self.update_deletion_balance(node.parent, node.is_left_child())

    def __delitem__(self, key):
        self.delete(key)


class TreeNode:
    def __init__(self, key, value, left=None, right=None, parent=None):
        self.key = key
        self.value = value
        self.left_child = left
        self.right_child = right
        self.parent = parent
        self.balance_factor = 0

    def has_left_child(self):
        return self.left_child

    def has_right_child(self):
        return self.right_child

    def is_left_child(self):
        return self.parent and self.parent.left_child == self

    def is_right_child(self):
        return self.parent and self.parent.right_child == self

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not self.left_child and not self.right_child

    def has_any_child(self):
        return self.left_child or self.right_child

    def has_both_child(self):
        return self.left_child and self.right_child

    def replace_node_data(self, key, value, left_child, right_child):
        self.key = key
        self.value = value
        self.left_child = left_child
        self.right_child = right_child
        if self.has_left_child():
            self.left_child.parent = self
        if self.has_right_child():
            self.right_child.parent = self

    def find_successor(self):
        return self.right_child.find_min()

    def find_min(self):
        current_node = self
        while current_node.has_left_child():
            current_node = current_node.left_child
        return current_node

    def splice_out(self):
        if self.is_leaf():
            if self.is_left_child():
                self.parent.left_child = None
            else:
                self.parent.right_child = None
        else:
            if self.is_left_child():
                self.right_child.parent = self.parent
                self.parent.left_child = self.right_child
            else:
                self.right_child.parent = self.parent
                self.parent.right_child = self.right_child

    def __iter__(self):
        if self:
            if self.has_left_child():
                for element in self.left_child:
                    yield element
            yield self.key
            if self.has_right_child():
                for element in self.right_child:
                    yield element


def main():
    tree = AVLTree()
    tree[2] = '21'
    tree[7] = '11'
    tree[11] = '666'
    tree[1] = '1'
    tree[6] = '211'

    for node_key in tree:
        print('中序遍历 node_key:', node_key)

    print(tree.root.key)
    print(tree[2])
    print(len(tree))
    print(7 in tree)
    del tree[7]
    print(tree[7])
    print(tree.root.key)


if __name__ == '__main__':
    main()
