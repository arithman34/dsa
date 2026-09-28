class Node:
    def __init__(self, value: object) -> None:
        self.value = value
        self.next: Node | None = None

    def __repr__(self) -> str:
        return f"Node({self.value})"


class LinkedList:
    def __init__(self) -> None:
        self._head: Node | None = None
        self._length: int = 0

    def __len__(self):
        return self._length

    def _check_index(self, index: int) -> None:
        if not 0 <= index < self._length:
            raise IndexError(index)

    def _check_insert_index(self, index: int) -> None:
        if not 0 <= index <= self._length:
            raise IndexError(index)

    def _traverse_to_index(self, index: int) -> Node:
        i = 0
        current = self._head
        while current is not None and i < index:
            i += 1
            current = current.next
        
        return current

    def prepend(self, value: object) -> None:
        new_node = Node(value)
        new_node.next = self._head
        self._head = new_node
        self._length += 1

    def append(self, value: object) -> None:
        if self._length == 0:
            self.prepend(value)
            return

        new_node = Node(value)
        tail = self._traverse_to_index(self._length - 1)
        tail.next = new_node
        tail = new_node
        self._length += 1

    def insert(self, index: int, value: object) -> None:
        self._check_insert_index(index)

        if index == 0:
            self.prepend(value)
            return
        if index == self._length:
            self.append(value)
            return

        new_node = Node(value)
        node = self._traverse_to_index(index - 1)
        new_node.next = node.next
        node.next = new_node
        self._length += 1

    def pop(self, index: int | None = None) -> None:
        if index is None:
            index = self._length - 1

        self._check_index(index)
        if index == 0:
            self._head = self._head.next
            self._length -= 1
            return
        elif index == self._length - 1:
            node = self._traverse_to_index(index - 1)
            node.next = None
            self._length -= 1
            return

        node = self._traverse_to_index(index - 1)
        node.next = node.next.next
        self._length -= 1

    def remove(self, value: object) -> None:
        current = self._head
        previous = None
        while current is not None:
            if current.value == value:
                if previous is None:
                    self._head = current.next
                else:
                    previous.next = current.next
                self._length -= 1
                return

            previous = current
            current = current.next

    def remove_all(self, value: object) -> None:
        current = self._head
        previous = None
        while current is not None:
            if current.value == value:
                if previous is None:
                    self._head = current.next
                else:
                    previous.next = current.next
                self._length -= 1
                current = current.next
                continue

            previous = current
            current = current.next

    def reverse(self) -> None:
        previous = None
        current = self._head
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        self._head = previous

    def __repr__(self) -> str:
        current = self._head
        arr = []
        while current is not None:
            arr.append(current.value)
            current = current.next

        return f"LinkedList({arr})"


def main():
    ll = LinkedList()
    ll.append(5)
    ll.append(7)
    ll.append(12)
    ll.append(13)

    ll.insert(3, 100)
    ll.pop(len(ll) - 1)

    print(ll)

if __name__ == "__main__":
    main()