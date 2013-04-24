# coding: utf-8

def permutation(string):
    if len(string) <= 1:
        return [string]
    arr = permutation(string[1:])
    res = []
    for elem in arr:
        for i in range(len(elem)+1):
            new_str = elem[0:i] + string[0] + elem[i:]
            res.append(new_str)
    return res 


if __name__ == "__main__":
    perms = permutation("abcdefghi")

    for p in perms:
        print p
