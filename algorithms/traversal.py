from data_structures.bst import BST

def bfs(tree: BST) -> list:
    current = tree.root
    if current is None:
        return []
    
    queue = []
    arr = []
    queue.append(current)

    while len(queue) > 0:
        current = queue.pop(0)
        arr.append(current.value)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return arr

def pre_order(tree: BST) -> list:
    arr = []

    def _pre_order(node):
        if node is None:
            return

        arr.append(node.value)
        _pre_order(node.left)
        _pre_order(node.right)

    _pre_order(tree.root)
    return arr

def in_order(tree: BST) -> list:
    arr = []

    def _in_order(node):
        if node is None:
            return

        _in_order(node.left)
        arr.append(node.value)
        _in_order(node.right)

    _in_order(tree.root)
    return arr

def post_order(tree: BST) -> list:
    arr = []

    def _post_order(node):
        if node is None:
            return

        _post_order(node.left)
        _post_order(node.right)
        arr.append(node.value)

    _post_order(tree.root)
    return arr
