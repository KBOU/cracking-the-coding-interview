def binary_search(arr, x, left, right):
    if left > right:
        return -1
    mid = (left + right) / 2
    if x < arr[mid]:
        return binary_search(arr, x, left, mid - 1)
    elif x > arr[mid]:
        return binary_search(arr, x, mid + 1, right)
    else:
        return mid

if __name__ == "__main__":
    arr = [0, 1, 3, 4]
    print binary_search(arr, 0, 0, len(arr) - 1)
    print binary_search(arr, 1, 0, len(arr) - 1)
    print binary_search(arr, 4, 0, len(arr) - 1)
    print binary_search(arr, 3, 0, len(arr) - 1)
