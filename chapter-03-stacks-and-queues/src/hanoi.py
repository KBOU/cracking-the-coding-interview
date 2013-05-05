# coding: utf-8

class Disk(object):
    def __init__(self, size):
        self.size = size
        self.last_moved = False

class HanoiTower(object):
    def __init__(self):
        self.__stack = []

    def push(self, disk):
        if len(self.__stack) == 0:
            self.__stack.append(disk)
            return
        top = self.__stack[len(self.__stack)-1]
        if top.size > disk.size:
            self.__stack.append(disk)
        else:
            raise Exception("top smaller than disk")

    def pop(self):
        if len(self.__stack) > 0:
            return self.__stack.pop()
        return None

    def peek(self):
        if len(self.__stack) > 0:
            return self.__stack[len(self.__stack)-1]
        return None

    def size(self):
        return len(self.__stack)

    def display(self, index):
        if index >= len(self.__stack):
            print "     ",
            return False
        print "  %d  " % self.__stack[index].size,
        return True

    def __str__(self):
        return self.__stack.__str__()

class Deck(object):
    def __init__(self, disk_num):
        self.__towers = [HanoiTower(), HanoiTower(), HanoiTower()]

        for size in range(disk_num, 0, -1):
            disk = Disk(size)
            self.__towers[0].push(disk)
        self.__goal = 1
        self.__last_goal = disk_num
        self.__goal_just_achieved = True
        self.__goal_tower = self.__towers[2] if disk_num % 2 == 1 else self.__towers[1]

    def move(self):
        if self.__goal > self.__last_goal:
            print "finished"
            return
        if self.__goal_just_achieved:
            (frm, to) = self.__find_move_goal_just_achieved()
        else:
            (frm, to) = self.__find_move_largest_and_not_moved()
        self.__reset_last_moved()

        disk = frm.pop()
        disk.last_moved = True
        to.push(disk)

        self.__check_goal_achieved()
        self.display()

    def display(self):
        fin = False
        i = 0
        while not fin:
            fin = True
            for tower in self.__towers:
                displayable = tower.display(i)
                if displayable:
                    fin = False
            i += 1
            print

    def __find_move_goal_just_achieved(self):
        return (self.__towers[0], self.__goal_tower)

    def __reset_last_moved(self):
        for tower in self.__towers:
            disk = tower.peek()
            if disk is not None:
                disk.last_moved = False

    def __check_goal_achieved(self):
        if self.__goal_tower.size() == self.__goal:
            self.__goal_just_achieved = True
            self.__goal += 1
            self.__goal_tower = self.__towers[2] if self.__goal_tower == self.__towers[1] else self.__towers[1]
        else:
            self.__goal_just_achieved = False

    def __find_move_largest_and_not_moved(self):
        move_from = None
        for tower in self.__towers:
            disk = tower.peek()
            if disk is not None and not disk.last_moved:
                if move_from is None:
                    move_from = tower
                elif disk.size < move_from.peek().size:
                    move_from = tower

        move_tos = []
        for tower in self.__towers:
            if tower is not move_from and (tower.peek() is None or tower.peek().size > move_from.peek().size):
                move_tos.append(tower)
        if len(move_tos) == 2:
            d0 = move_tos[0].peek()
            d1 = move_tos[1].peek()
            if d0 is not None:
                if (move_from.peek().size - d0.size) % 2 == 1:
                    move_to = move_tos[0]
                else:
                    move_to = move_tos[1]
            else:
                if (move_from.peek().size - d1.size) % 2 == 1:
                    move_to = move_tos[1]
                else:
                    move_to = move_tos[0]
        else:
            move_to = move_tos[0]
        return (move_from, move_to)


if __name__ == "__main__":
    import time

    deck = Deck(8)
    while True:
        deck.move()
        time.sleep(1)
