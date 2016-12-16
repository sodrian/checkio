def weak_point(matrix):
    row_sum = []
    column_sum = []

    for i, row in enumerate(matrix):
        row_sum.append(sum(row))
        for j, column in enumerate(row):
            
            if len(column_sum) <= j:
                column_sum.append(column)
            else:
                column_sum[j] += column
    
    min_row = min(row_sum)
    min_column = min(column_sum)
    
    return [row_sum.index(min_row), column_sum.index(min_column)]


if __name__ == '__main__':
    assert isinstance(weak_point([[1]]), (list, tuple)), "The result should be a list or a tuple"
    assert list(weak_point([[7, 2, 7, 2, 8],
                            [2, 9, 4, 1, 7],
                            [3, 8, 6, 2, 4],
                            [2, 5, 2, 9, 1],
                            [6, 6, 5, 4, 5]])) == [3, 3], "Example"
    assert list(weak_point([[7, 2, 4, 2, 8],
                            [2, 8, 1, 1, 7],
                            [3, 8, 6, 2, 4],
                            [2, 5, 2, 9, 1],
                            [6, 6, 5, 4, 5]])) == [1, 2], "Two weak point"
    assert list(weak_point([[1, 1, 1],
                            [1, 1, 1],
                            [1, 1, 1]])) == [0, 0], "Top left"
