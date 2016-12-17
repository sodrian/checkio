FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):
    out = []

    hundred_part = number // 100
    ten_part = number % 100 // 10
    solitary_part = number % 100 % 10

    if hundred_part:
        out.append(FIRST_TEN[hundred_part-1])
        out.append(HUNDRED)

    if ten_part:
        if ten_part == 1:
            out.append(SECOND_TEN[solitary_part])
        elif ten_part >= 2:
            out.append(OTHER_TENS[ten_part-2])

    if solitary_part and (ten_part == 0 or ten_part in range(2, 10)):
        out.append(FIRST_TEN[solitary_part-1])

    return ' '.join(out)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
