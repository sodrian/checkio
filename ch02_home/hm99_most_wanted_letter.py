import string


def checkio(text):
    d = {}
    for l in text.lower():
        if l in string.ascii_lowercase:
            d[l] = d.get(l, 0) + 1

    mx = (None, 0)
    for k, v in d.items():
        if v > mx[1]:
            mx = (k, v)
        elif v == mx[1] and k < mx[0]:
            mx = (k, v)

    return mx[0]


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
