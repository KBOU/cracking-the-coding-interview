# coding; utf-8
import math

all_patterns = []

def add_columns(row, columns):
    if row == len(columns):
        all_patterns.append(columns[:])

    for col in range(len(columns)):
        if check_valid(row, col, columns):
            columns[row] = col
            add_columns(row + 1, columns)

def check_valid(row, col, columns):
    for r in range(row):
        col2 = columns[r]
        if col2 == col:
            return False
        if math.fabs(col2 - col) == math.fabs(row - r):
            return False
    return True


if __name__ == "__main__":
    add_columns(0, [0] * 8)
    for k, pat in enumerate(all_patterns):
        print "PATTERN %d" % k
        for i in range(8):
            for j in range(8):
                ch = " "
                if pat[i] == j:
                    ch = "Q"
                print "|%s" % ch,
            print "|"
            print " - " * 8

        print
