OPERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")
IMPLICATION_MATRIX = {
    (False, False): True,
    (False, True): True,
    (True, False): False,
    (True, True): True}


def boolean(x, y, operation):
    if operation == OPERATION_NAMES[0]:
        return x and y
    elif operation == OPERATION_NAMES[1]:
        return x or y
    elif operation == OPERATION_NAMES[2]:
        return IMPLICATION_MATRIX[(x, y)]
    elif operation == OPERATION_NAMES[3]:
        return x != y
    elif operation == OPERATION_NAMES[4]:
        return x == y


if __name__ == '__main__':
    assert boolean(1, 0, "conjunction") == 0, "and"
    assert boolean(1, 0, "disjunction") == 1, "or"
    assert boolean(1, 1, "implication") == 1, "material"
    assert boolean(0, 1, "exclusive") == 1, "xor"
    assert boolean(0, 1, "equivalence") == 0, "same?"
