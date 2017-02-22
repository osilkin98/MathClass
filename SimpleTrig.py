from math import pi
from math import radians
from math import sin
from math import asin
from math import cos
from math import acos
from math import tan
from math import atan
'''asin(oppo/hypo) = radians'''
'''print (180*asin(oppo/hypo)/pi)  from radians to degree'''


def sin_opposite(angle, hypo):  # to find opposite using sin
    opposite = sin(radians(angle))*hypo
    return opposite


def sin_hypo(angle, opposite):  # to find hypo using sin
    hypo = opposite / (sin(radians(angle)))
    return hypo


def sin_angle(opposite, hypo):  # to find the angle using sin
    angle = (180 * (asin(opposite / hypo)) / pi)
    return angle


def cos_adjacent(angle, hypo):  # to find opposite using cos
    adjacent = cos(radians(angle))*hypo
    return adjacent


def cos_hypo(angle, adjacent):  # to find hypo using cos
    hypo = adjacent / (cos(radians(angle)))
    return hypo


def cos_angle(adjacent, hypo):  # to find the angle using cos
    angle = (180*acos(adjacent/hypo)/pi)
    return angle


def tan_opposite(angle, adjacent):  # to find opposite using tan
    opposite = tan(radians(angle)) * adjacent
    return opposite


def tan_adjacent(angle, opposite):  # to find adjacent using tan
    adjacent = opposite / (tan(radians(angle)))
    return adjacent


def tan_angle(opposite, adjacent):  # to find the angle using tan
    angle = (180*atan(opposite/adjacent)/pi)
    return angle


''' gives you a formal state of your angle 43.859 -> 43.86'''


def formal_angle(angle):
    dig_to_rnd = (int(angle * 1000)) % 10  # digit to round
    if dig_to_rnd > 10:  # if the angle has only one digit before the decimal point
        dig_to_rnd = int(dig_to_rnd / 10)
        new_angle = float(int(angle * 10)) / 10
    else:
        new_angle = float(int(angle * 100)) / 100
    if dig_to_rnd > 5:
        new_angle += 0.01
    return new_angle
