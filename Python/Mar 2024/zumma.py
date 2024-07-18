class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def insert(self, root, data):
        if not root:
            return Node(data)
        elif data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)

        # Left Left Case
        if balance > 1 and data < root.left.data:
            return self.right_rotate(root)

        # Right Right Case
        if balance < -1 and data > root.right.data:
            return self.left_rotate(root)

        # Left Right Case
        if balance > 1 and data > root.left.data:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right Left Case
        if balance < -1 and data < root.right.data:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def delete(self, root, data):
        if not root:
            return root

        elif data < root.data:
            root.left = self.delete(root.left, data)

        elif data > root.data:
            root.right = self.delete(root.right, data)

        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.get_min_value_node(root.right)
            root.data = temp.data
            root.right = self.delete(root.right, temp.data)

        if root is None:
            return root

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)

        # Left Left Case
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)

        # Left Right Case
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right Right Case
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)

        # Right Left Case
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def search(self, root, data):
        if not root or root.data == data:
            return root
        if data < root.data:
            return self.search(root.left, data)
        return self.search(root.right, data)

    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def get_min_value_node(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current

    def in_order_traversal(self, root):
        if root is None:
            return []
        return self.in_order_traversal(root.left) + [root.data] + self.in_order_traversal(root.right)

    def pre_order_traversal(self, root):
        if root is None:
            return []
        return [root.data] + self.pre_order_traversal(root.left) + self.pre_order_traversal(root.right)

    def post_order_traversal(self, root):
        if root is None:
            return []
        return self.post_order_traversal(root.left) + self.post_order_traversal(root.right) + [root.data]

    def print_tree(self, root, level=0, is_left=None):
        if root is None:
            return

        if level == 0:
            print(f"Root: {root.data} [Height: {root.height}, Balance: {self.get_balance(root)}]")
        else:
            if is_left:
                print(" " * (level * 4) + "|__ L: " + f"{root.data} [Height: {root.height}, Balance: {self.get_balance(root)}]")
            else:
                print(" " * (level * 4) + "|__ R: " + f"{root.data} [Height: {root.height}, Balance: {self.get_balance(root)}]")

        self.print_tree(root.left, level + 1, True)
        self.print_tree(root.right, level + 1, False)


# Example Usage:
avl = AVLTree()
root = None

# Insert elements into the AVL tree
root = avl.insert(root, 10)
root = avl.insert(root, 20)
root = avl.insert(root, 30)
# root = avl.insert(root, 40)
# root = avl.insert(root, 50)
# root = avl.insert(root, 25)
# print(root.left.left.data)
print("AVL tree after insertion:")
avl.print_tree(root)
