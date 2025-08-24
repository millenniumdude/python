class Node:
    def __init__(self, key=None, left = None, right = None):
        self.key = key
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None

    # Insert a node

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self._insert(root.left, key)
        else:
            root.right = self._insert(root.right, key)
        return root

    # 1. In class BST, define a method to find minimum value item node.

    def find_min(self):
        current = self.root
        if current is None:
            return None
        while current.left:
            current = current.left
        return current.key

    # 2. In class BST, define a method to find maximum value item node.

    def find_max(self):
        current = self.root
        if current is None:
            return None
        while current.right:
            current = current.right
        return current.key

    # 3. In class BST, define a method to delete a node from binary search tree.

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if root is None:
            return root
        if key < root.key:
            root.left = self._delete(root.left, key)
        elif key > root.key:
            root.right = self._delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp = self._find_min_node(root.right)
            root.key = temp.key
            root.right = self._delete(root.right, temp.key)
        return root

    def _find_min_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    # 4. In class BST, define a method size to return the number of elements present in the BST.

    def size(self):
        return self._size(self.root)

    def _size(self, node):
        if node is None:
            return 0
        return 1 + self._size(node.left) + self._size(node.right)

    # 5. In class BST, define a method to implement inorder traversal.(Left, Root, Right)

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.key)
            self._inorder(node.right, result)

    # 6. In class BST, define a method to implement preorder traversal.(Root, Left, Right)

    def preorder(self):
        result = []
        self._preorder(self.root, result)
        return result

    def _preorder(self, node, result):
        if node:
            result.append(node.key)
            self._preorder(node.left, result)
            self._preorder(node.right, result)

    # 7. In class BST, define a method to implement postorder traversal.(Left, Right, Root)

    def postorder(self):
        result = []
        self._postorder(self.root, result)
        return result

    def _postorder(self, node, result):
        if node:
            self._postorder(node.left, result)
            self._postorder(node.right, result)
            result.append(node.key)

# Example

bst = BST()
for value in [50, 30, 70, 20, 40, 60, 80]:
    bst.insert(value)

print("Inorder Traversal:", bst.inorder())      
print("Preorder Traversal:", bst.preorder())    
print("Postorder Traversal:", bst.postorder())  
print("Min:", bst.find_min())                   
print("Max:", bst.find_max())   
print("The size of the BST is:", bst.size())                
#bst.delete(70)
#print("Tree deletion:", bst.inorder()) 