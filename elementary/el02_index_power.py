def index_power(array, n):
    """
        Find Nth power of the element with index N.
    """
    try:
        ret = array[n] ** n
    except IndexError:
        ret = -1

    return ret


if __name__ == '__main__':
    assert index_power([1, 2, 3, 4], 2) == 9, "Square"
    assert index_power([1, 3, 10, 100], 3) == 1000000, "Cube"
    assert index_power([0, 1], 0) == 1, "Zero power"
    assert index_power([1, 2], 3) == -1, "IndexError"
