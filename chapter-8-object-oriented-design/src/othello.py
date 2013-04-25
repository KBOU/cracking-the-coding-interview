# coding: utf-8

import sys
import re

class Board(object):
    __WIDTH = 8
    __HEIGHT = 8

    __instance = None

    __board = None
    __players = None
    __turn = True
    __possible = []

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(Board, cls).__new__(cls)
            cls.__board = [None] * cls.__WIDTH * cls.__HEIGHT
            cls.__players = [Player(True), Player(False)]
            for i in range(cls.__WIDTH * cls.__HEIGHT - 4):
                if i % 2 == 0:
                    piece = Piece(True)
                    cls.__players[0].pieces.append(piece)
                else:
                    piece = Piece(False)
                    cls.__players[1].pieces.append(piece)
            cls.__board[cls.__convert_to_index(3, 3)] = Piece(True)
            cls.__board[cls.__convert_to_index(3, 4)] = Piece(False)
            cls.__board[cls.__convert_to_index(4, 4)] = Piece(True)
            cls.__board[cls.__convert_to_index(4, 3)] = Piece(False)
        return cls.__instance
    def __init__(self):
        pass

    @classmethod
    def start_game(cls):
        cls.display()

    @classmethod
    def display(cls):
        cls.__display_board()
        if cls.is_next_possible():
            (x, y) = Prompt().get_command()
            if cls.__turn:
                cls.__players[0].put(x, y)
            else:
                cls.__players[1].put(x, y)
        else:
            cls.finish()

    @classmethod
    def can_put(cls, x, y):
        for elem in cls.__possible:
            if elem[0] == x and elem[1] == y:
                return True

        return False
    @classmethod
    def reverse(cls, piece, x, y):
        cls.__board[cls.__convert_to_index(x, y)] = piece
        cls.__reverse_check_horizontal(x, y)
        cls.__reverse_check_vertical(x, y)
        cls.__reverse_check_diagonal_down(x, y)
        cls.__reverse_check_diagonal_up(x, y)
        cls.__do_reverse()
        cls.__reset_candidates()

        cls.__turn = not cls.__turn
        cls.display()

    @classmethod
    def is_next_possible(cls):
        possible = False
        cls.__possible = []
        for i in range(cls.__WIDTH * cls.__HEIGHT):
            if cls.__board[i] is not None:
                continue
            (x, y) = cls.__convert_to_grid(i)
            cls.__reverse_check_horizontal(x, y)
            cls.__reverse_check_vertical(x, y)
            cls.__reverse_check_diagonal_down(x, y)
            cls.__reverse_check_diagonal_up(x, y)
            for piece in cls.__board:
                if piece is not None and piece.reverse_candidate:
                    cls.__reset_candidates()
                    print "possible", chr(ord('a') + x), y+1
                    cls.__possible.append([x, y])
                    possible = True

        cls.__reset_candidates()
        return possible

    @classmethod
    def count(cls, white):
        cnt = 0
        for piece in cls.__board:
            if piece is not None and piece.white is True:
                cnt += 1
        return cnt

    @classmethod
    def finish(cls):
        white = cls.count(True)
        black = cls.count(False)
        if white > black:
            bye = "White wins"
        elif white < black:
            bye = "Black wins"
        else:
            bye = "Draw"

        print "%s\nBye!!" % bye

    @classmethod
    def __convert_to_grid(cls, index):
        return (index % cls.__WIDTH, index / cls.__WIDTH)
    @classmethod
    def __convert_to_index(cls, x, y):
        return y * cls.__WIDTH + x

    @classmethod
    def __find_nearest_friend(cls, x, y, default):
        piece = cls.__board[cls.__convert_to_index(x, y)]
        if piece is None:
            return (True, default, default)
        if piece.white is cls.__turn:
            return (True, x, y)
        return (False, default, default)

    @classmethod
    def __set_candidate(cls, x, y):
        piece = cls.__board[cls.__convert_to_index(x, y)]
        if piece is not None and piece.white is not cls.__turn:
            piece.reverse_candidate = True
    @classmethod
    def __reverse_check_horizontal(cls, x, y):
        start = x 
        xi = x - 1

        while xi >= 0:
            (fin, start, tmp) = cls.__find_nearest_friend(xi, y, start)
            if fin:
                break
            xi -= 1
        for xi in range(start, x):
            cls.__set_candidate(xi, y)

        start = x
        xi = x + 1
        while xi < cls.__WIDTH:
            (fin, start, tmp) = cls.__find_nearest_friend(xi, y, start)
            if fin:
                break
            xi += 1
        for xi in range(x + 1, start):
            cls.__set_candidate(xi, y)

    @classmethod
    def __reverse_check_vertical(cls, x, y):
        start = y 
        yi = y - 1

        while yi >= 0:
            (fin, tmp, start) = cls.__find_nearest_friend(x, yi, start)
            if fin:
                break
            yi -= 1
        for yi in range(start, y):
            cls.__set_candidate(x, yi)

        start = y
        yi = y + 1
        while yi < cls.__HEIGHT:
            (fin, tmp, start) = cls.__find_nearest_friend(x, yi, start)
            if fin:
                break
            yi += 1
        for yi in range(y + 1, start):
            cls.__set_candidate(x, yi)


    @classmethod
    def __reverse_check_diagonal_down(cls, x, y):
        start = x 
        xi = x - 1
        yi = y - 1

        while xi >= 0 and yi >= 0:
            (fin, start, tmp) = cls.__find_nearest_friend(xi, yi, start)
            if fin:
                break
            xi -= 1
            yi -= 1
        for xi in range(start, x):
            yi = y - (x - xi)
            cls.__set_candidate(xi, yi)

        start = x
        xi = x + 1
        yi = y + 1
        while xi < cls.__WIDTH and yi < cls.__HEIGHT:
            (fin, start, tmp) = cls.__find_nearest_friend(xi, yi, start)
            if fin:
                break
            xi += 1
            yi += 1
        for xi in range(x + 1, start):
            yi = y - (x + 1 - xi)
            cls.__set_candidate(xi, yi)

    @classmethod
    def __reverse_check_diagonal_up(cls, x, y):
        start = x 
        xi = x - 1
        yi = y + 1

        while xi >= 0 and yi < cls.__HEIGHT:
            (fin, start, tmp) = cls.__find_nearest_friend(xi, yi, start)
            if fin:
                break
            xi -= 1
            yi += 1
        for xi in range(start, x):
            yi = y + (x - xi)
            cls.__set_candidate(xi, yi)

        start = x
        xi = x + 1
        yi = y - 1
        while xi < cls.__WIDTH and yi >= 0:
            (fin, start, tmp) = cls.__find_nearest_friend(xi, yi, start)
            if fin:
                break
            xi += 1
            yi -= 1
        for xi in range(x + 1, start):
            yi = y + (x + 1 - xi)
            cls.__set_candidate(xi, yi)

    @classmethod
    def __do_reverse(cls):
        for piece in cls.__board:
            if piece is not None and piece.reverse_candidate:
                piece.white = not piece.white

    @classmethod
    def __reset_candidates(cls):
        for piece in cls.__board:
            if piece is not None:
                piece.reverse_candidate = False

    @classmethod
    def __display_board(cls):
        print "   a  b  c  d  e  f  g  h "
        print " ",
        print " _ " * cls.__WIDTH

        for i in range(cls.__WIDTH * cls.__HEIGHT):
            (x, y) = cls.__convert_to_grid(i)
            if cls.__board[i] is None:
                ch = " "
            else:
                ch = cls.__board[i].icon()
            if x % cls.__WIDTH == 0:
                print y + 1,
            print "|%s" % ch,
            if x == cls.__WIDTH - 1:
                print "|"
                print " ",
                print " _ " * cls.__WIDTH
        print
        print
        print



class Player(object):
    def __init__(self, white):
        self.white = white
        self.pieces = []

    def put(self, x, y):
        Board().reverse(self.pieces.pop(), x, y)

class Piece(object):
    def __init__(self, white):
        self.white = white
        self.reverse_candidate = False

    def icon(self):
        if self.white:
            return "o"
        else:
            return "x"

class Prompt(object):
    __instance = None
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(Prompt, cls).__new__(cls)
        return cls.__instance

    def __init__(self):
        pass

    @classmethod
    def get_command(cls):
        print "input position: ",
        while True:
            inp = sys.stdin.readline()
            try:
                (x, y) = CommandParser().parse(inp.strip())
                return (x, y)
            except CommandParseError:
                print "cannot parse input again: ",
            except OverrideError:
                print "cannot put theare: ",

class CommandParser(object):
    __instance = None
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(CommandParser, cls).__new__(cls)
        return cls.__instance

    def __init__(self):
        pass

    @classmethod
    def parse(cls, inp):
        if len(inp) < 2 or re.match("[a-h][1-8]", inp) is None:
            raise CommandParseError 
        else:
            (x, y) = (ord(inp[0]) - ord("a"), int(inp[1]) - 1)
            if Board().can_put(x, y):
                return (x, y)
            else:
                raise OverrideError 

class CommandParseError(Exception):
    pass
class OverrideError(Exception):
    pass

if __name__ == "__main__":
    Board().start_game()
