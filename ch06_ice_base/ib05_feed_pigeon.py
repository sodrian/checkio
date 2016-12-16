def checkio(number):
    minute = 0
    cur_pigeons = 0
    fed_pigeons = 0

    while True:
        minute += 1
        cur_pigeons += minute
        number -= cur_pigeons

        if number > 0:
            fed_pigeons = cur_pigeons
        else:
            fed_pigeons = max(cur_pigeons + number, fed_pigeons)
            break

    return fed_pigeons


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(1) == 1, "1st example"
    assert checkio(2) == 1, "2nd example"
    assert checkio(5) == 3, "3rd example"
    assert checkio(10) == 6, "4th example"