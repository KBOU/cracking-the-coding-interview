# coding: utf-8
bitfields = [0] * (1 << 12)
def find_dup(arr):
    for el in arr:
        bit = (bitfields[el / 8] >> (el % 8)) & 1
        if bit == 1:
            print el
        else:
            bitfields[el / 8] |= 1 << el % 8

if __name__ == "__main__":
    find_dup([1, 1, 1, 2, 3, 4, 4, 2, 6, 6, 5, 4, 3])
