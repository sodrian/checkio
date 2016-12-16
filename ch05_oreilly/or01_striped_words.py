import re

VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"


def checkio(text):
    if len(text) == 0:
        return 0

    ret = 0
    words = re.split(r'\W+', text)
    words = [w for w in words if len(w) >= 2]

    for w in words:
        even_letters = w[::2]
        odd_letters = w[1::2]

        if all([l.upper() in VOWELS for l in even_letters]) and \
                all([l.upper() in CONSONANTS for l in odd_letters]) or \
                all([l.upper() in CONSONANTS for l in even_letters]) and \
                all([l.upper() in VOWELS for l in odd_letters]):
            ret += 1

    return ret


if __name__ == '__main__':
    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
