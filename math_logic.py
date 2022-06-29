import math as mt

def Equals(input):
    if '-' in input:
        lsst = input.split('-')
        first = float(lsst[0])
        second = float(lsst[1])
        minus = first - second
        return minus
    elif '+' in input:
        lsst = input.split('+')
        first = float(lsst[0])
        second = float(lsst[1])
        plus = first + second
        return plus
    elif '/' in input:
        lsst = input.split('/')
        first = float(lsst[0])
        second = float(lsst[1])
        division = first / second
        return division

    elif '*' in input:
        lsst = input.split('*')
        first = float(lsst[0])
        second = float(lsst[1])
        multip = first * second
        return multip

    elif 'j' in input:
        lsst = input.replace('j','')
        lsst = list(map(int, lsst.split('+')))
        first = complex(lsst[0], lsst[1])
        second = complex(lsst[2],lsst[3])
        cmplx_sum = first + second
        return cmplx_sum

