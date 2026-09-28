def bubble_sort(arr):
    for i in range(len(arr)):
        swapped = False
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break
    
    return arr

def selection_sort(arr):
    for i in range(len(arr)):
        smallest = i
        for j in range(i, len(arr)):
            if arr[j] < arr[smallest]:
                smallest = j
            
        arr[i], arr[smallest] = arr[smallest], arr[i]

    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        current = arr[i]
        j = i - 1
        while j >= 0 and current < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = current

    return arr

def merge_sort(arr):
    length = len(arr)
    if length < 2:
        return arr

    middle = length // 2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])

    return _merge(left, right)

def _merge(left, right):
    arr = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr.append(left[i])
            i += 1
        else:
            arr.append(right[j])
            j += 1

    arr.extend(left[i:])
    arr.extend(right[j:])
    return arr

def quick_sort(arr):
    if len(arr) < 2:
        return arr

    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    middle = [x for x in arr if x == pivot]

    return quick_sort(left) + middle + quick_sort(right)

print(merge_sort([6, 2, 7, 3, 10, 5, 1, 8]))