# coding: utf-8

class Box:
    def __init__(self, w, h, d):
        self.w = w
        self.h = h
        self.d = d

    def __cmp__(self, other):
        return self.h - other.h

    def __str__(self):
        return str(self.w) + ", " + str(self.h) + ", " + str(self.d)

CHAINS = []
HIGHEST = [0]

def tallest_box(boxes, prev, index, chain, remain, height=0):
    if index > len(boxes) - 1:
        if height >= HIGHEST[0]:
            CHAINS.append(chain)
        return
    if index == 0:
        remain = sum(b.h for b in boxes)

    if height + remain <= HIGHEST[0]:
        return

    remain -= boxes[index].h
    if index == 0 or (boxes[prev].w > boxes[index].w and boxes[prev].d > boxes[index].d):
        height += boxes[index].h
        if HIGHEST[0] < height:
            HIGHEST[0] = height
        ch = chain[:]
        ch.append(boxes[index])
        tallest_box(boxes, index, index+1, ch, remain, height)
    else:
        ch = chain[:]
        tallest_box(boxes, index-1, index+1, ch, remain, height)
        ch = []
        ch.append(boxes[index])
        tallest_box(boxes, index, index+1, ch, remain, boxes[index].h)



if __name__ == "__main__":
    values = (
        (100, 200, 50),
        (90, 220, 100),
        (120, 300, 80),
        (100, 400, 95),
    )

    boxes = []
    for val in values:
        boxes.append(Box(*val))

    boxes.sort()
    boxes.reverse()
    tallest_box(boxes, 0, 0, [], 0)
    print HIGHEST[0]


