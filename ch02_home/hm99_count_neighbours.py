def count_neighbours(grid, row, col):
    grd_len = len(grid)

    neighb_sum = 0
    row_range = []
    col_range = []

    for k in range(-1, 2):
        if row + k in range(0, grd_len):
            row_range.append(row + k)
        if col + k in range(0, grd_len):
            col_range.append(col + k)

    for i in row_range:
        for j in col_range:
            if i == row and j == col:
                continue
            try:
                neighb_sum += grid[i][j]
            except IndexError:
                pass

    return neighb_sum


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 1, 2) == 3, "1st example"
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 0, 0) == 1, "2nd example"
    assert count_neighbours(((1, 1, 1),
                             (1, 1, 1),
                             (1, 1, 1),), 0, 2) == 3, "Dense corner"
    assert count_neighbours(((0, 0, 0),
                             (0, 1, 0),
                             (0, 0, 0),), 1, 1) == 0, "Single"
