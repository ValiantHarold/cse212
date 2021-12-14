class BST:
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = BST.Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, node):

        if node is None:
            return BST.Node(data)

        if data < node.data:
            node.left = self._insert(data, node.left)
            return node
        elif data > node.data:
            node.right = self._insert(data, node.right)
            return node
        else:
            return node

    def get_height(self):
        pass

    def _get_height(self, node):
        pass


tree = BST()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(4)
tree.insert(10)
tree.insert(1)
tree.insert(6)

print(tree.get_height())  # 3
tree.insert(6)
print(tree.get_height())  # 3
tree.insert(12)
print(tree.get_height())  # 4
