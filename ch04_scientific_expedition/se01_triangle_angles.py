import math


def checkio(a, b, c):
    if a + b <= c or \
        a + c <= b or \
        b + c <= a:
        return [0, 0, 0]

    alfa = math.acos( (a**2 - b**2 - c**2) / (2*b*c*-1))
    beta = math.acos((b**2 - a**2 - c**2) / (2*a*c*-1))
    gamma = math.acos((c**2 - a**2 - b**2) / (2*a*b*-1))
    alfa, beta, gamma = math.degrees(alfa), math.degrees(beta), math.degrees(gamma)
    alfa, beta, gamma = round(alfa), round(beta), round(gamma)
    
    ret = [alfa, beta, gamma]
    ret.sort()
    
    return ret
    

if __name__ == '__main__':
    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"
