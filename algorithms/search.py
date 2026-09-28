def linear_search(arr: list, target: object) -> bool:
    for value in arr:
        if value == target:
            return True

    return False

def binary_search(arr: list, target: object) -> bool:
    left = 0
    right = len(arr) - 1
    while left <= right:
        middle = (left + right) // 2
        if target == arr[middle]:
            return True
        elif target < arr[middle]:
            right = middle - 1
        else:
            left = middle + 1

    return False
