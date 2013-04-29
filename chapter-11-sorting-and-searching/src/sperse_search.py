def sperse_search(arr, x, left, right):
    if left > right:
        return -1
    mid = (left + right) / 2

    if arr[mid] ==  "":
        l = mid - 1
        r = mid + 1
        while True:
            if l < left and r > right:
                return -1
            if l >= left and arr[l] != "":
                mid = l
                break
            if r <= right and arr[r] != "":
                mid = r
                break
            l -= 1
            r += 1
    if x < arr[mid]:
        sperse_search(arr, x, left, mid-1)
    elif x > arr[mid]:
        sperse_search(arr, x, mid+1, right)
    else:
        return mid
