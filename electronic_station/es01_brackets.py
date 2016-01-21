OPENING_BRACKETS = '([{'
CLOSING_BRACKETS = ')]}'


def checkio(expression):
    stack = []

    for el in expression:
        if el in OPENING_BRACKETS:
            stack.append(el)
        elif el in CLOSING_BRACKETS:
            try:
                st_el = stack.pop()
                if OPENING_BRACKETS.find(st_el) != CLOSING_BRACKETS.find(el):
                    return False
            except IndexError:
                return False

    return len(stack) == 0


if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"
