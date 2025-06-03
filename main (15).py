class Node:
    def __init__(self): 
        self.left = None
        self.right = None
        self.data = None

    def inorder_traversal(self, Node):
        if Node:
            self.inorder_traversal(Node.left)
            print(Node.data)
            self.inorder_traversal(Node.right)

    def preorder_traversal(self, Node):
        if Node:
            print(Node.data)
            self.preorder_traversal(Node.left)
            self.preorder_traversal(Node.right)

    def postorder_traversal(self, Node):
        if Node:
            self.postorder_traversal(Node.left) 
            self.postorder_traversal(Node.right)
            print(Node.data)

    def sum_of_nodes(self, Node):
        if Node is None:
            return 0
        return Node.data + self.sum_of_nodes(Node.left) + self.sum_of_nodes(Node.right)

    def height(self, Node):
        if Node is None:
            return 0
        else:
            return 1 + max(self.height(Node.left), self.height(Node.right))  

tree = Node()
tree.data = 1
tree.left = Node()
tree.left.data = 2
tree.right = Node()
tree.right.data = 3
tree.right.left = Node()
tree.right.left.data = 6
tree.right.right = Node()
tree.right.right.data = 7

print("Inorder Traversal:")
tree.inorder_traversal(tree)
print("\nPreorder Traversal:")
tree.preorder_traversal(tree)
print("\nPostorder Traversal:")
tree.postorder_traversal(tree)
print("\nSum of nodes:")
print(tree.sum_of_nodes(tree))  
print("\nHeight of tree:")
print(tree.height(tree))
