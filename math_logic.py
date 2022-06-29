import math as mt

def Equals(input):
    if '-' in input:
        lsst = input.split('-')
        if '.' in lsst[0] or '.' in lsst[1]:
            first = float(lsst[0])
            second = float(lsst[1])
            minus = first - second
            return minus
        else:
            first = int(lsst[0])
            second = int(lsst[1])
            minus = first - second
            return minus
    elif '+' in input:
        lsst = input.split('+')
        if '.' in lsst[0] or '.' in lsst[1]:
            first = float(lsst[0])
            second = float(lsst[1])
            plus = first + second
            return plus
        else:
            first = int(lsst[0])
            second = int(lsst[1])
            plus = first + second
            return plus

    elif '/' in input:
        lsst = input.split('/')
        first = float(lsst[0])
        second = float(lsst[1])
        division = first / second
        if first % second == 0:
            return int(division)
        else:
            return division

    elif '*' in input:
        lsst = input.split('*')
        first = float(lsst[0])
        second = float(lsst[1])
        multip = first * second
        if str(multip)[-2:] =='.0':
            return int(multip)
        else:
            return multip

def Complex(a, j1, b, j2, index):
    first = complex(int(a), int(j1))
    second = complex(int(b), int(j2))
    if index == 0:
        cmplx_sum = first + second
        return cmplx_sum
    elif index == 1:
        cmplx_sum = first - second
        return cmplx_sum
    elif index == 2:
        cmplx_sum = first / second
        return cmplx_sum
    elif index == 3:
        cmplx_sum = first * second
        return cmplx_sum
