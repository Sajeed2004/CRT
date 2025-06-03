class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None

tree = Node()
tree.data = 1
tree.left = Node()
tree.left.data = 2

tree.right = Node()
tree.right.data = 3
print(tree.data)
print(tree.left.data)
print(tree.right.data)
        