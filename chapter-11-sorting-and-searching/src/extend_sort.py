# coding: utf-8

def merge_sort(a, left, mid, right):
    cloned = a[:]

    cnt = left
    leftCnt = left
    rightCnt = mid

    while leftCnt < mid and rightCnt <= right:
        if cloned[leftCnt] < cloned[rightCnt]:
            a[cnt] = cloned[leftCnt]
            leftCnt += 1
        else:
            a[cnt] = cloned[rightCnt]
            rightCnt += 1
        cnt += 1

    while leftCnt < mid:
        a[cnt] = cloned[leftCnt]
        leftCnt += 1
        cnt += 1


def extend_sort(a, b):
    left = 0
    right = len(a) + len(b) - 1
    mid = len(a)

    a.extend(b)

    merge_sort(a, left, mid, right)


if __name__ == "__main__":
    a = [0, 2, 4, 5]
    b = [1, 3]
    extend_sort(a, b)
    print a
