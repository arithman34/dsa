class Array:
    def __init__(self, capacity: int) -> None:
        self._capacity: int = capacity
        self._values: list[object] = [None] * capacity

    def _check_index(self, index: int) -> None:
        if not 0 <= index < self._capacity:
            raise IndexError(index)

    def __getitem__(self, index: int) -> object:
        self._check_index(index)
        return self._values[index]

    def __setitem__(self, index: int, value: object) -> None:
        self._check_index(index)
        self._values[index] = value

    def __len__(self) -> int:
        return self._capacity

    def __repr__(self) -> str:
        return f"Array([{[value for value in self._values if value is not None]}])"
