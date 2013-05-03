# coding; utf-8

TREE = []

def parens(num, index=0, left_in=0, right_in=0, total=0, wk_str=""):
    if index == num * 2:
        if total != 0:
            raise ValueError
        TREE.append(wk_str)
        return
    if index == 0:
        parens(num, index + 1, left_in + 1, right_in, total + 1, wk_str + "(")
    elif index == num * 2 - 1:
        parens(num, index + 1, left_in, right_in + 1, total - 1, wk_str + ")")
    else:
        if left_in < num:
            parens(num, index + 1, left_in + 1, right_in, total + 1, wk_str + "(")
        if right_in < num and total >= 1:
            parens(num, index + 1, left_in, right_in + 1, total - 1, wk_str + ")")


if __name__ == "__main__":
    parens(5)
    print TREE
