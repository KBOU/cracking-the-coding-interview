# coding: utf8

import sys

class JigsawPuzzle(object):
    __ingame = True
    __frame = []
    __workspace = []
    __player = None

    def __new__(cls, *arg, **kwargs):
        if not hasattr(cls, "__instance__"):
            cls.__instance__ = super(JigsawPuzzle, cls).__new__(cls)
            # プレーヤー
            cls.__player = Player()

            # ピースの初期化
            width = arg[0]
            height = arg[1]
            piece_num = width * height
            cls.__frame = [None] * piece_num
            for i in range(0, height):
                for j in range(0, width):
                    pid = i * width + j
                    top_id = pid - width if (pid - width) >= 0 else None
                    bottom_id = pid + width if (pid + width) <= (width * height) else None
                    left_id = pid - 1 if (pid % width) != 0 else None
                    right_id = pid + 1 if ((pid + 1) % width) != 0 else None
                    cls.__workspace.append(Piece(pid, top_id, bottom_id, left_id, right_id))
        return cls.__instance__

    def __init__(self, *arg, **kwargs):
        pass

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
            cls.__workspace[index] = piece
        else:
            cls.__frame[index] = piece

        if cls.finished():
            cls.done()

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

    def fitswith(self, piece):
        # TODO fitするかチェック
        pass

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
