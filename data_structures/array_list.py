class ArrayList:
    def __init__(self) -> None:
        self._capacity: int = 1
        self._length: int = 0
        self._values: list[object] = [None]

    def _check_index(self, index: int) -> None:
        if not 0 <= index < self._length:
            raise IndexError(index)

    def _check_insert_index(self, index: int) -> None:
            if not 0 <= index <= self._length:
                raise IndexError(index)

    def __getitem__(self, index: int) -> object:
        self._check_index(index)
        return self._values[index]

    def __setitem__(self, index: int, value: object) -> None:
        self._check_index(index)
        self._values[index] = value

    def _resize(self, capacity: int) -> None:
        # Allocate new array
        new_values: list[object] = [None] * capacity

        # Copy
        for i in range(self._length):
            new_values[i] = self._values[i]

        # Swap references
        self._values = new_values
        self._capacity = capacity

    def _lshift(self, index: int) -> None:
        for i in range(index, self._length - 1):
            self._values[i] = self._values[i + 1]

    def _rshift(self, index: int) -> None:
        for i in range(self._length, index, -1):
            self._values[i] = self._values[i - 1]

    def append(self, value: object) -> None:
        if self._length == self._capacity:
            self._resize(self._capacity * 2)

        self._values[self._length] = value
        self._length += 1

    def pop(self, index: int | None = None) -> object:
        if index is None:
            index = self._length - 1

        self._check_index(index)
        item = self._values[index]
        self._lshift(index)
        self._values[self._length - 1] = None
        self._length -= 1
        return item

    def insert(self, index: int, value: object) -> None:
        self._check_insert_index(index)
        if self._length == self._capacity:
            self._resize(self._capacity * 2)

        self._rshift(index)
        self._values[index] = value
        self._length += 1

    def remove(self, value: object) -> None:
        for i, v in enumerate(self._values):
            if i == self._length:
                break
            if v == value:
                self.pop(i)
                return

        raise ValueError("ArrayList.remove(x): x not in list")

    def __len__(self) -> int:
        return self._length

    def __repr__(self) -> str:
        return f"ArrayList({[value for value in self._values if value is not None]})"
    