def checkio(n, m):
    n = str(bin(n))[2:]
    m = str(bin(m))[2:]

    if len(n) > len(m):
        m = m.zfill(len(n))
    elif len(m) > len(n):
        n = n.zfill(len(m))

    ret = 0
    for i in range(len(n)):
        if n[i] != m[i]:
            ret += 1

    return ret


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(117, 17) == 3, "First example"
    assert checkio(1, 2) == 2, "Second example"
    assert checkio(16, 15) == 5, "Third example"
