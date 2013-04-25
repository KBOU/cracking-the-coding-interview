# coding: utf-8

ORIGINAL_COLOR = []

def fill_color(screen, pixel, new_color, first=True):
    if first:
        ORIGINAL_COLOR.append(screen[pixel[0]][pixel[1]])

    for i in range(-1, 2):
        for j in range(-1, 2):
            y = pixel[0] - i
            x = pixel[1] - j
            if y >= 0 and y < len(screen) and x >= 0 and x < len(screen[y]):
                if screen[y][x] == ORIGINAL_COLOR[0]:
                    screen[y][x] = new_color
                    fill_color(screen, (x, y), new_color, False)
                    


if __name__ == "__main__":
    screen = [
        ["g", "r", "r", "g", "r"],
        ["r", "r", "r", "g", "r"],
        ["r", "r", "g", "g", "g"],
        ["g", "g", "g", "g", "r"],
        ["r", "r", "g", "r", "r"]
    ]
    pixel = (2, 2)
    new_color = "b"

    print "### ORIGINAL ###"
    for y in screen:
        print y
    print
    print

    fill_color(screen, pixel, new_color)

    print "### FILLED ###"
    for y in screen:
        print y
