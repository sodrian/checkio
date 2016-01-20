from datetime import date, timedelta


def checkio(from_date, to_date):
    rt = 0

    dff = to_date - from_date
    dff = dff.days

    for i in range(dff + 1):
        dt = from_date + timedelta(days=i)
        if dt.isoweekday() in [6, 7]:
            rt += 1

    return rt


if __name__ == '__main__':
    assert checkio(date(2013, 9, 18), date(2013, 9, 23)) == 2, "1st example"
    assert checkio(date(2013, 1, 1), date(2013, 2, 1)) == 8, "2nd example"
    assert checkio(date(2013, 2, 2), date(2013, 2, 3)) == 2, "3rd example"

