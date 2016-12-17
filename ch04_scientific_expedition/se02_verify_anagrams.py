import string


def verify_anagrams(first_word, second_word):
    first_word = [l.lower() for l in first_word if l in string.ascii_letters]
    second_word = [l.lower() for l in second_word if l in string.ascii_letters]

    if len(first_word) != len(second_word):
        return False

    are_anagramms = True

    for l in first_word:
        try:
            second_word.remove(l)
        except ValueError:
            are_anagramms = False
            break

    return are_anagramms


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(verify_anagrams("a", 'z'), bool), "Boolean!"
    assert verify_anagrams("Programming", "Gram Ring Mop") == True, "Gram of code"
    assert verify_anagrams("Hello", "Ole Oh") == False, "Hello! Ole Oh!"
    assert verify_anagrams("Kyoto", "Tokyo") == True, "The global warming crisis of 3002"

