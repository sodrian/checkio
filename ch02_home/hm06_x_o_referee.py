class XOException(Exception):
    pass


def check_seq(seq):
    if isinstance(seq, (list, tuple)):
        seq = ''.join(seq)
    if all([x == 'X' for x in seq]):
        raise XOException('X')
    elif all([x == 'O' for x in seq]):
        raise XOException('O')


def checkio(game_result):
    try:
        # checking rows
        for i in range(3):
            check_seq(game_result[i])

        # checking columns
        for j in range(3):
            seq = []
            for i in range(3):
                seq.append(game_result[i][j])
            check_seq(seq)

        # checking diagonal
        seq = [game_result[k][k] for k in range(3)]
        check_seq(seq)

        # checking another diagonal
        seq = [game_result[2-l][l] for l in range(3)]
        check_seq(seq)

    except XOException as err:
        return err.args[0]

    else:
        return "D"


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"

