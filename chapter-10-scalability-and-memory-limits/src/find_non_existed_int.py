# coding: utf-8

bitfields = [0] * 1048576
blocks = [0] * 4096

def find_int():
    fl = open("integers.txt", "r")
    for line in fl:
        line = line.strip()
        num = int(line)
        blocks[num / len(blocks)] += 1

    for i, block in enumerate(blocks):
        if block < len(bitfields):
            start = i * len(bitfields)
            break

    for i, line in enumerate(fl):
        if i >= start and i < start + len(bitfields)
            bitfields[(i - start) / 8] |= 1 << (i - start) % 8

    for i, byte in enumerate(bitfields):
        for j in range(8):
            if (byte & 1 << j) == 0:
                print i * 8 + j, "lacks"
                break
