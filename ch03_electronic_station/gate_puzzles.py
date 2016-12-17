import re


def calc_res(w1, w2):
    ret = 0.0

    if w1[0] == w2[0]:
        ret += .1
    if w1[-1] == w2[-1]:
        ret += .1
    if len(w1) <= len(w2):
        ret += (len(w1) / len(w2)) * .3
    else:
        ret += (len(w2) / len(w1)) * .3

    common_letters = set(w1) & set(w2)
    unique_letters = set(w1) | set(w2)

    ret += (len(common_letters) / len(unique_letters)) * .5

    print(w1, w2, ret)

    return ret


def find_word(message):
    words = re.split(r'\W+', message)
    words = [word.lower() for word in words if word]
    
    resemblanes = []

    for i, w1 in enumerate(words):
        sum_res = 0
        for j, w2 in enumerate(words):
            if i != j:
                sum_res += calc_res(w1, w2)
        resemblanes.append(sum_res)
    
    print(resemblanes)    
    
    indx = max((el, i) for i, el in enumerate(resemblanes))[1]

    return words[indx]


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_word("Speak friend and enter.") == "friend", "Friend"
    assert find_word("Beard and Bread") == "bread", "Bread is Beard"
    assert find_word("The Doors of Durin, Lord of Moria. Speak friend and enter. "
                     "I Narvi made them. Celebrimbor of Hollin drew these signs") == "durin", "Durin"
    assert find_word("Aoccdrnig to a rscheearch at Cmabrigde Uinervtisy."
                     " According to a researcher at Cambridge University.") == "according", "Research"
    assert find_word("One, two, two, three, three, three.") == "three", "Repeating"
