def checkio(words_set):
    ln_set = len(words_set)
    words_set = list(words_set)
    for i in range(0, ln_set - 1):
        for j in range(i+1, ln_set):
            if words_set[i].endswith(words_set[j]) or \
                    words_set[j].endswith(words_set[i]):
                return True
    else:
        return False


if __name__ == '__main__':
    assert checkio({"hello", "lo", "he"}) == True, "helLO"
    assert checkio({"hello", "la", "hellow", "cow"}) == False, "hellow la cow"
    assert checkio({"walk", "duckwalk"}) == True, "duck to walk"
    assert checkio({"one"}) == False, "Only One"
    assert checkio({"helicopter", "li", "he"}) == False, "Only end"
