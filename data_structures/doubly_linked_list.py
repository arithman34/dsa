class Node:
    def __init__(self, value):
        self._value = value
        self._next = None
        self._prev = None

class DoublyLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0

    def __len__(self):
        return self._length

    def _check_index(self, index: int) -> None:
        if not 0 <= index < self._length:
            raise IndexError(index)

    # def prepend(self, value):
    #     new_node = Node(value)
        