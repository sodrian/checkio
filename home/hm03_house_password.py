import string


def checkio(data):
    return len(data) >= 10 and \
        any(l in string.ascii_lowercase for l in data) and \
        any(l in string.ascii_uppercase for l in data) and \
        any(l in string.digits for l in data)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
