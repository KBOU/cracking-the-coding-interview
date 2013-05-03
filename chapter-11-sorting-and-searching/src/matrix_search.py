def horizontal_search(matrix, x, col, start_row, end_row):
    if start_row > end_row:
        return None
    mid = (start_row + end_row) / 2

    if x < matrix[col][mid]:
        return horizontal_search(matrix, x, col, start_row, mid - 1)
    elif x > matrix[col][mid]:
        return horizontal_search(matrix, x, col, mid + 1, end_row)
    else:
        return (col, mid)

def vertical_search(matrix, x, row, start_col, end_col):
    if start_col > end_col:
        return None
    mid = (start_col + end_col) / 2

    if x < matrix[mid][row]:
        return vertical_search(matrix, x, row, start_col, mid - 1)
    elif x > matrix[mid][row]:
        return vertical_search(matrix, x, row, mid + 1, end_col)
    else:
        return (col, mid)
    
def matrix_search(matrix, x, top_left, bottom_right):
    (start_col, start_row) = top_left
    min_delta = min(bottom_right[0] - start_col, bottom_right[1] - start_row)
    (end_col, end_row) = (start_col + min_delta, start_row + min_delta)

    if start_col < 0 or start_row < 0:
        return None
    if end_col > len(matrix) or end_row > len(matrix[0]):
        return None

    if top_left[0] == bottom_right[0]:
        return horizontal_search(matrix, x, start_col, top_left[1], bottom_right[1])
    elif top_left[1] == bottom_right[1]:
        return vertical_search(matrix, x, start_row, top_left[0], bottom_right[0])

    while start_col <= end_col:
        mid_col = (start_col + end_col) / 2
        mid_row = (start_row + end_row) / 2
        if x > matrix[mid_col][mid_row]:
            start_col += 1
            start_row += 1
        elif x < matrix[mid_col][mid_row]:
            end_col -= 1
            end_row -= 1
        else:
            return (mid_col, mid_row)
    
    ret = matrix_search(matrix, x, (top_left[0], start_row), (start_col-1, bottom_right[1]))
    if ret is None:
        ret = matrix_search(matrix, x, (start_col, top_left[1]), (bottom_right[0], start_row-1))
    return ret

if __name__ == "__main__":
    matrix = [
        [1, 2, 3, 4, 5],
        [2, 4, 6, 8, 10],
        [3, 6, 9, 12, 15],
        [4, 8, 12, 16, 20]
    ]
    print matrix_search(matrix, 3, (0, 0), (3, 4))
