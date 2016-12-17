def count_inversion(sequence):
    """
        Count inversions in a sequence of numbers
    """
    ln_sq = len(sequence)
    cnt = 0
    for i in range(0, ln_sq - 1):
        for j in range(i + 1, ln_sq):
            if sequence[i] > sequence[j]:
                cnt += 1
    return cnt


if __name__ == '__main__':
    assert count_inversion((1, 2, 5, 3, 4, 7, 6)) == 3, "Example"
    assert count_inversion((0, 1, 2, 3)) == 0, "Sorted"
    assert count_inversion((99, -99)) == 1, "Two numbers"
    assert count_inversion((5, 3, 2, 1, 0)) == 10, "Reversed"
