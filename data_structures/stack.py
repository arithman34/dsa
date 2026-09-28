class Stack:
    def __init__(self) -> None:
        self._values = []

    def __len__(self) -> int:
        return len(self._values)

    def is_empty(self) -> bool:
        return len(self) == 0

    def push(self, value: object) -> None:
        self._values.append(value)

    def pop(self) -> object | None:
        if self.is_empty():
            return None
        
        return self._values.pop()

    def peek(self) -> object | None:
        if self.is_empty():
            return None
        
        return self._values[len(self) - 1]

    def __repr__(self) -> str:
        return f"Stack({self._values})"
