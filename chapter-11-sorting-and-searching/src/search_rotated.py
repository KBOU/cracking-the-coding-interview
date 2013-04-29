# coding: utf-8

def search_rotated_index(rotated, left, right):
    if left == right:
        return -1

    if rotated[left] > rotated[right]:
        mid = (left + right) / 2
        l = search_rotated_index(rotated, left, mid)
        r = search_rotated_index(rotated, mid + 1, right)
        if l == -1 and r == -1:
            return mid + 1
        else:
            return l if l > r else r
    else:
        return -1

def bin_search(arr, x, left, right):
    if left > right:
        return -1
    mid = (left + right) / 2

    if x < arr[mid]:
        return bin_search(arr, x, left, mid - 1)
    elif x > arr[mid]:
        return bin_search(arr, x, mid + 1, right)
    else:
        return mid

def search_rotated(rotated, x, left, right):
    rotated_index = search_rotated_index(rotated, 0, len(rotated) - 1)
    arr = rotated[rotated_index:] + rotated[:rotated_index]
    print arr
    index = bin_search(arr, x, left, right)
    return (rotated_index + index) % len(rotated)


if __name__ == "__main__":
    arr = [5, 0, 1, 2, 3, 4]
    print search_rotated(arr, 5, 0, len(arr) - 1)

