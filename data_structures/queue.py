class Node:
    def __init__(self, value: object) -> None:
        self.value: object = value
        self.next: Node | None = None

    def __repr__(self) -> str:
        return f"Node({self.value})"

class Queue:
    def __init__(self) -> None:
        self._front: Node | None = None
        self._rear: Node | None = None
        self._length: int = 0

    def __len__(self) -> int:
        return self._length

    def is_empty(self) -> bool:
        return self._front is None

    def enqueue(self, value: object) -> None:
        new_node = Node(value)
        if self.is_empty():
            self._front = self._rear = new_node
            self._length += 1
            return
        
        self._rear.next = new_node
        self._rear = new_node
        self._length += 1

    def dequeue(self) -> object | None:
        if self.is_empty():
            return None

        node = self._front
        self._front = self._front.next
        self._length -= 1
        if self.is_empty():
            self._rear = None
        return node.value

    def peek(self) -> object | None:
        if self.is_empty():
            return None
        
        return self._front.value

    def __repr__(self) -> str:
        current = self._front
        arr = []
        while current is not None:
            arr.append(current.value)
            current = current.next

        return f"Queue({arr})"

class QueueWithStacks:
    def __init__(self):
        from stack import Stack
        self._in_stack = Stack()
        self._out_stack = Stack()

    def __len__(self) -> int:
        return len(self._in_stack) + len(self._out_stack)

    def is_empty(self) -> bool:
        return len(self) == 0

    def _move(self) -> None:
        if self._out_stack.is_empty():
            while not self._in_stack.is_empty():
                self._out_stack.push(self._in_stack.pop())

    def enqueue(self, value):
        self._in_stack.push(value)

    def dequeue(self) -> object | None:
        if self.is_empty():
            return None

        self._move()
        return self._out_stack.pop()

    def peek(self) -> object | None:
        if self.is_empty():
            return None

        self._move()
        return self._out_stack.peek()

    def __repr__(self):
        front_to_back = list(reversed(self._out_stack._values)) + self._in_stack._values
        return f"QueueUsingStacks({front_to_back})"
