# coding: utf-8

CACHE = {}

def factorial(x):
    if x <= 1:
        return 1
    return x * factorial(x - 1)
def combination(x, y):
    return factorial(x + y) / (factorial(x) * factorial(y))

def combination_ext(x, y):
    key = str(x) + "_" + str(y)
    if CACHE.get(key) is not None:
        return CACHE.get(key)

    # もし行き止まりがあれば、
    # ここでreturn 0すればいい

    if x == 0:
        return 1
    if y == 0:
        return 1

    CACHE[key] = combination_ext(x - 1, y) + combination_ext(x, y - 1)
    return CACHE[key]

if __name__ == "__main__":
    print combination(100,28)
    print combination_ext(100,28)
