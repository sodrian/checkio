def checkio(number):
    number = str(number)
    prod = 1
    for el in number:
        if el != '0':
            prod *= int(el)
    return prod


if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
