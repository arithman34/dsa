class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self) -> str:
        return f"Node({self.value})"

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return

        current = self.root
        while current is not None:
            if value < current.value:
                if current.left is None:
                    current.left = new_node
                    return

                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return

                current = current.right

    def remove(self, value: object) -> bool:
        if self.root is None:
            return False
        
        current = self.root
        parent = None
        while current is not None:
            if value < current.value:
                parent = current
                current = current.left
            elif value > current.value:
                parent = current
                current = current.right
            else:
                if current.right is None and current.left is None:  # Case 1: leaf
                    if parent is None:
                        self.root = None
                    elif current is parent.left:
                        parent.left = None
                    else:
                        parent.right = None
                elif current.right is None or current.left is None:  # Case 2: one child
                    child = current.left if current.left is not None else current.right
                    if parent is None:
                        self.root = child
                    elif current is parent.left:
                        parent.left = child
                    else:
                        parent.right = child
                else:  # Case 3: two children
                    successor_parent = current
                    successor = current.right
                    while successor.left is not None:
                        successor_parent = successor
                        successor = successor.left

                    current.value = successor.value

                    if successor is successor_parent.left:
                        successor_parent.left = successor.right
                    else:
                        successor_parent.right = successor.right

                return True

        return False

    def search(self, value: object) -> bool:
        if self.root is None:
            return False
        
        current = self.root
        while current is not None:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return False

    def in_order(self):
        arr = []

        def _in_order(node):
            if node is None:
                return
            
            _in_order(node.left)
            arr.append(node.value)
            _in_order(node.right)

        _in_order(self.root)
        return arr
