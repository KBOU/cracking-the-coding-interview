def bubble_sort(arr):
    finished = False
    while not finished:
        finished = True
        for i in range(len(arr) - 1):
            if arr[i] > arr[i+1]:
                (arr[i], arr[i+1]) = (arr[i+1], arr[i])
                finished = False

def selection_sort(arr):
    for i in range(len(arr) - 1):
        smallest_index = i
        smallest = arr[i]
        for j in range(i+1, len(arr)):
            if arr[j] < smallest:
                smallest_index = j
                smallest = arr[j]
        if smallest_index != i:
            (arr[i], arr[smallest_index]) = (arr[smallest_index], arr[i])

def merge(arr, left, mid, right):
    cloned = arr[:]
    leftCnt = left
    rightCnt = mid + 1
    cnt = left
    while leftCnt <= mid and rightCnt <= right:
        if cloned[leftCnt] > cloned[rightCnt]:
            arr[cnt] = cloned[rightCnt]
            rightCnt += 1
        else:
            arr[cnt] = cloned[leftCnt]
            leftCnt += 1
        cnt += 1
    for i in range(leftCnt, mid):
        arr[cnt] = cloned[leftCnt]
        leftCnt += 1
        cnt += 1

def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) / 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid+1, right)
        merge(arr, left, mid, right)

def quick(arr, left, right):
    pivot = arr[(left + right) / 2]

    while left <= right:
        while arr[left] < pivot:
            left += 1
        while arr[right] > pivot:
            right -= 1

        if left <= right:
            (arr[left], arr[right]) = (arr[right], arr[left])
            left += 1
            right -= 1
    return left
    
def quick_sort(arr, left, right):
    index = quick(arr, left, right)
    print left, right, index
    if left < index - 1:
        quick_sort(arr, left, index - 1)
    if index < right:
        quick_sort(arr, index, right)

if __name__ == "__main__":
    arr = [
        1, 4, 2, 3, 5, 2, 3, 8, 9
    ]
    #bubble_sort(arr)
    #selection_sort(arr)
    #merge_sort(arr, 0, len(arr)-1)
    quick_sort(arr, 0, len(arr)-1)
    print arr
