# coding: utf-8

def subset(arr):
    if len(arr) == 0:
        return arr
    elif len(arr) == 1:
        return [[], arr]

    arr_a = subset(arr[0:1])
    arr_b = subset(arr[1:])

    subsets = []
    for aelem in arr_a:
        for belem in arr_b:
            elem = []
            elem.extend(aelem)
            elem.extend(belem)
            subsets.append(elem)
    return subsets


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    subsets = subset(arr)
    for sset in subsets:
        print sset
    print "total = %d" % len(subsets)
