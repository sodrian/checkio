def fib(i):
    if i == 0:
        return 1
    elif i == 1:
        return 1
    elif i >= 2:
        return fib(i-1) + fib(i-2)
    else:
        return 0


FIB_LIST = [fib(i) for i in range(20)]


def ghost_years():
    ret = []
    opacity = 10000
    ret.append(opacity)
    for i in range(1, 5000):
        if i in FIB_LIST:
            opacity -= i
        else:
            opacity += 1
        ret.append(opacity)
    return ret

GHOST_YEARS = ghost_years()


def checkio(opacity):
    try:
        return GHOST_YEARS.index(opacity)
    except ValueError:
        return None


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(10000) == 0, "Newborn"
    assert checkio(9999) == 1, "1 year"
    assert checkio(9997) == 2, "2 years"
    assert checkio(9994) == 3, "3 years"
    assert checkio(9995) == 4, "4 years"
    assert checkio(9990) == 5, "5 years"