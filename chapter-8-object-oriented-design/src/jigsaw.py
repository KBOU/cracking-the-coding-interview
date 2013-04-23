# coding: utf8

import sys

class JigsawPuzzle(object):
    __ingame = True
    __frame = []
    __workspace = []
    __player = None
    TOP = 0
    BOTTOM = 1
    LEFT = 2
    RIGHT = 3

    def __new__(cls, *arg, **kwargs):
        if not hasattr(cls, "__instance__"):
            cls.__instance__ = super(JigsawPuzzle, cls).__new__(cls)
            # プレーヤー
            cls.__player = Player()

            # ピースの初期化
            cls.width = arg[0]
            cls.height = arg[1]
            piece_num = cls.width * cls.height
            cls.__frame = [None] * piece_num
            for i in range(0, cls.height):
                for j in range(0, cls.width):
                    pid = i * cls.width + j
                    top_id = cls.get_top_id(pid)
                    bottom_id = cls.get_bottom_id(pid)
                    left_id = cls.get_left_id(pid)
                    right_id = cls.get_right_id(pid)
                    cls.__workspace.append(Piece(pid, top_id, bottom_id, left_id, right_id))
        return cls.__instance__

    def __init__(self, *arg, **kwargs):
        pass

    @classmethod
    def get_top_id(cls, pid):
        return pid - cls.width if (pid - cls.width) >= 0 else None
    @classmethod
    def get_bottom_id(cls, pid):
       return pid + cls.width if (pid + cls.width) < (cls.width * cls.height) else None
    @classmethod
    def get_left_id(cls, pid):
       return pid - 1 if (pid % cls.width) != 0 else None
    @classmethod
    def get_right_id(cls, pid):
       return pid + 1 if ((pid + 1) % cls.width) != 0 else None

    @classmethod
    def start_game(cls):
        while cls.__ingame:
            cls.display_stat()
            cls.mainloop()

    @classmethod
    def display_stat(cls):
        print "frame:", cls.__frame
        print "workspace:", cls.__workspace

    @classmethod
    def mainloop(cls):
        print "choose piece:", 
        (iswk, index) = cls.parse_command(sys.stdin.readline().strip())
        cls.__player.choose_piece(iswk, index)

        print "set piece:", 
        (iswk, index) = cls.parse_command(sys.stdin.readline().strip())
        cls.__player.set_piece(iswk, index)

    @classmethod
    def parse_command(cls, line):
        (iswk, index) = line.split(" ")
        iswk = False if iswk is "f" else True
        index = int(index)
        return (iswk, index)

    @classmethod
    def shuffle(cls):
        # TODO シャッフル機能
        pass

    @classmethod
    def get_piece(cls, iswk, index):
        cls.__wk_space = iswk
        cls.__wk_index = index
        if iswk:
            piece = cls.__workspace[index]
            cls.__workspace[index] = None
        else:
            piece = cls.__frame[index]
            cls.__frame[index] = None
        return piece

    @classmethod
    def set_piece(cls, piece, iswk, index):
        if iswk:
            prev = cls.__workspace[index]
            cls.__workspace[index] = piece
        else:
            prev = cls.__frame[index]
            cls.__frame[index] = piece

        if cls.__wk_space:
            cls.__workspace[cls.__wk_index] = prev
        else:
            cls.__frame[cls.__wk_index] = prev
            


        for i, piece in enumerate(cls.__frame):
            if piece is not None:
                top_id = cls.get_top_id(i)
                bottom_id = cls.get_bottom_id(i)
                left_id = cls.get_left_id(i)
                right_id = cls.get_right_id(i)
                if top_id is not None:
                    fit = cls.fitswith(piece, cls.__frame[top_id], cls.TOP)
                    if fit:
                        piece.top_fit = True
                        cls.__frame[top_id].bottom_fit = True
                if bottom_id is not None:
                    fit = cls.fitswith(piece, cls.__frame[bottom_id], cls.BOTTOM)
                    if fit:
                        piece.bottom_fit = True
                        cls.__frame[bottom_id].top_fit = True
                if left_id is not None:
                    fit = cls.fitswith(piece, cls.__frame[left_id], cls.LEFT)
                    if fit:
                        piece.left_fit = True
                        cls.__frame[left_id].right_fit = True
                if right_id is not None:
                    fit = cls.fitswith(piece, cls.__frame[right_id], cls.RIGHT)
                    if fit:
                        piece.right_fit = True
                        cls.__frame[right_id].left_fit = True

        if cls.finished():
            cls.done()

    @classmethod
    def fitswith(cls, p1, p2, direction):
        if p2 is None:
            return False

        if direction is cls.TOP:
            expected_id = cls.get_top_id(p1.self_id)
        elif direction is cls.BOTTOM:
            expected_id = cls.get_bottom_id(p1.self_id)
        elif direction is cls.LEFT:
            expected_id = cls.get_left_id(p1.self_id)
        elif direction is cls.RIGHT:
            expected_id = cls.get_right_id(p1.self_id)
        else:
            expected_id = -1
        return p2.self_id is expected_id

    @classmethod
    def finished(cls):
        for piece in cls.__frame:
            if piece is None or not piece.done():
                return False
        return True

    @classmethod
    def done(cls):
        print "frame:", cls.__frame
        print "workspace:", cls.__workspace
        print "CONGRATULATIONS!!!"
        cls.__ingame = False

class Piece(object):
    def __init__(self, self_id, top_id, bottom_id, left_id, right_id):
        self.self_id = self_id
        self.top_piece_id = top_id
        self.bottom_piece_id = bottom_id
        self.left_piece_id = left_id
        self.right_piece_id = right_id

        self.top_fit = False if not top_id is None else True
        self.bottom_fit = False if not bottom_id is None else True
        self.left_fit = False if not left_id is None else True
        self.right_fit = False if not right_id is None else True

    def done(self):
        print self.top_fit, self.bottom_fit, self.left_fit, self.right_fit
        return self.top_fit and self.bottom_fit and self.left_fit and self.right_fit

    def __repr__(self):
        return "%s(%d)" %  (self.__class__.__name__, self.self_id)

class Player(object):
    def __init__(self):
        self.piece = None

    def choose_piece(self, iswk, index):
        self.piece = JigsawPuzzle.get_piece(iswk, index)

    def set_piece(self, iswk, index):
        if self.piece is not None:
            JigsawPuzzle.set_piece(self.piece, iswk, index)
            self.piece = None

if __name__ == "__main__":
    jigsaw = JigsawPuzzle(2, 2)
    jigsaw.start_game()
