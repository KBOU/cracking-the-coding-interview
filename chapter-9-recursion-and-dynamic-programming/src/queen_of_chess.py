# coding; utf-8

from copy import deepcopy

BOARD = [[True] * 8] * 2
ALL_POS = []
def put_queens(board, index=0, queenpos=[]):
    if index >= len(board):
        return queenpos

    for i, cell in enumerate(board[index]):
        if cell:
            clone_board = deepcopy(board)
            pos = [i]
            for j in range(index + 1, len(clone_board)):
                clone_board[j][i] = False
                if i + j - index < len(clone_board[0]):
                    clone_board[j][i+j-index] = False
                if i - j - index >= 0:
                    clone_board[j][i-j-index] = False

            if len(queenpos) > 0:
                pos.extend(queenpos)
            put_queens(clone_board, index + 1, pos)

            if len(pos) == len(board):
                ALL_POS.append(pos)


if __name__ == "__main__":
    put_queens(BOARD)

    for i, pos in enumerate(ALL_POS):
        pos.reverse()
        print "CASE %d" % i
        print " - " * len(BOARD[0])
        for y in range(len(BOARD)):
            for x in range(len(BOARD[0])):
                ch = " "
                if pos[y] == x:
                    ch = "Q"
                print "|%s" % ch,
            print "|"
            print " - " * len(BOARD[0])
        print
