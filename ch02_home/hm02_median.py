def checkio(data):
    data.sort()

    ln = len(data)

    if ln == 0:
        return 0
    elif ln % 2 == 1:
        mdn = data[ln//2]
    else:
        mdn = (data[ln//2 - 1] + data[ln//2]) / 2.0

    return mdn


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([1, 2, 3, 4, 5]) == 3, "Sorted list"
    assert checkio([3, 1, 2, 5, 3]) == 3, "Not sorted list"
    assert checkio([1, 300, 2, 200, 1]) == 2, "It's not an average"
    assert checkio([3, 6, 20, 99, 10, 15]) == 12.5, "Even length"
    print("Start the long test")
    assert checkio(list(range(1000000))) == 499999.5, "Long."
    print("The local tests are done.")