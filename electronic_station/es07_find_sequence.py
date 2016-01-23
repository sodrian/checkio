def checkio(matrix):
    for i, row in enumerate(matrix):
        for j, column in enumerate(row):
            try:
                # to the right of the current element == 0 degrees
                if matrix[i][j] == matrix[i][j+1] == matrix[i][j+2] == matrix[i][j+3]:
                    print(matrix, 0)
                    return True

                # 45 degrees
                if matrix[i][j] == matrix[i+1][j+1] == matrix[i+2][j+2] == matrix[i+3][j+3]:
                    print(matrix, 45)
                    return True

                # 90 degrees
                if matrix[i][j] == matrix[i+1][j] == matrix[i+2][j] == matrix[i+3][j]:
                    print(matrix, 90)
                    return True

                # 135 degrees
                if matrix[i][j] == matrix[i+1][j-1] == matrix[i+2][j-2] == matrix[i+3][j-3]:
                    print(matrix, 135)
                    return True

                # 180 degrees
                if matrix[i][j] == matrix[i][j-1] == matrix[i][j-2] == matrix[i][j-3]:
                    print(matrix, 180)
                    return True

                # 225 degrees
                if matrix[i][j] == matrix[i-1][j-1] == matrix[i-2][j-2] == matrix[i-3][j-3]:
                    print(matrix, 225)
                    return True

                # 270 degrees
                if matrix[i][j] == matrix[i-1][j] == matrix[i][j-2] == matrix[i][j-3]:
                    print(matrix, 270)
                    return True

                # 315 degrees
                if matrix[i][j] == matrix[i-1][j+1] == matrix[i-2][j-2] == matrix[i-3][j-3]:
                    print(matrix, 315)
                    return True

            except IndexError:
                pass

    return False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True, "Vertical"
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False, "Nothing here"
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"
