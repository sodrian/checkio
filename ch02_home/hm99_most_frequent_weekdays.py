from datetime import date, timedelta

WEEKDAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


def get_all_maxes_indexes(lst):
    indx = []
    vls = []
    for i in range(len(lst)):
        if indx == []:
            indx.append(i)
            vls.append(lst[i])
        elif lst[i] == vls[0]:
            indx.append(i)
            vls.append(lst[i])
        elif lst[i] > vls[0]:
            indx = [i]
            vls = [lst[i]]
    return indx


def most_frequent_days(year):
    lst = [0] * 7

    dt = date(year=year, month=1, day=1)
    for i in range(367):
        if dt.year == year:
            lst[dt.weekday()] += 1
        dt = dt + timedelta(days=1)

    indexes = get_all_maxes_indexes(lst)
    ret = [WEEKDAYS[i] for i in indexes]

    return ret


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert most_frequent_days(2399) ==  ['Friday'], "1st example"
    assert most_frequent_days(1152) == ['Tuesday', 'Wednesday'], "2nd example"
    assert most_frequent_days(56) == ['Saturday', 'Sunday'], "3rd example"
    assert most_frequent_days(2909) == ['Tuesday'], "4th example"
