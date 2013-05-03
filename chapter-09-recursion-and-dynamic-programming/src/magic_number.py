# coding: utf-8

def magic_number(arr, index):
    print index, data
    if data < index:
        return magic_number(arr, index + 1)
    elif data == index:
        return True
    elif data > index:
        if data >= len(arr):
            return False
        return magic_number(arr, data)


if __name__ == "__main__":
    print magic_number([-2, 1, 2, 3, 4], 0)
