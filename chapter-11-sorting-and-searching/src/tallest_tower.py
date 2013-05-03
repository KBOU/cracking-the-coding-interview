# coding: utf-8

class Tower(object):
    def __init__(self):
        self.tower = []
    def push(self, man):
        if len(self.tower) == 0:
            self.tower.append(man)
            return True
        for i in range(len(self.tower)-1, -1, -1):
            m = self.tower[i]
            if m.height > man.height and m.weight > man.weight:
                self.tower.insert(i+1, man.clone())
                return True
            # ソートされてるのでほんとは通らないけど、
            # 仕様が変わっても対応できるように・・・
            if m.height < man.height and m.weight < man.weight:
                self.tower.insert(i, man.clone())
                return True
        return False

    def __cmp__(self, other):
        return len(self.tower) - len(other.tower)

    def __str__(self):
        pstr = "["
        for man in self.tower:
            pstr += "(" + str(man.height) + ", " + str(man.weight) + "),"
        pstr += "]"
        return pstr


class Man(object):
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    def __cmp__(self, other):
        return self.height - other.height
    def __str__(self):
        return "(" + str(self.height) + "," + str(self.weight) + ")"
    def clone(self):
        return Man(self.height, self.weight)


def tallest_tower(arr):
    men = []
    for elem in arr:
        men.append(Man(*elem))

    men.sort()
    men.reverse()

    towers = [Tower()]
    for man in men:
        pushed = False
        for tower in towers:
            pushable = tower.push(man)
            if pushable:
                pushed = pushable

        if not pushed:
            tower = Tower()
            tower.push(man)
            towers.append(tower)
    return max(towers)

if __name__ == "__main__":
    arr = (
            (65, 100),
            (70, 150),
            (56, 90),
            (75, 100),
            (60, 95),
            (68, 110))

    tower = tallest_tower(arr)
    print tower

