import csv
from decimal import Decimal, getcontext

getcontext().prec = 80

# These orbits contain all the unique step combinations for
# the values 1 to 512
orbits = [3, 9, 57, 135, 505, 153, 363, 447, 511, 261, 87,
          465, 489, 99, 397, 33, 177, 315, 39, 123, 493, 219,
          439, 279, 237, 357, 105, 421, 249, 393, 375, 477, 405,
          51, 273, 225, 451, 339, 255, 309, 117, 469, 45, 321, 507,
          483, 69, 369, 15, 81, 303, 159, 495, 111, 27, 171,
          457, 387, 291, 165, 231, 411, 487, 129, 459, 345, 195,
          147, 333, 327, 501, 189, 285, 429, 63, 417, 471, 399, 381,
          243, 103, 183, 207, 351, 297, 385, 435, 93, 441, 141, 213,
          21, 75, 267, 475, 453, 201, 423, 403]


def is_odd(number):
    return number % 2 != 0


def exponent(number, count=1):
    number = number / 2
    if is_odd(number):
        return count
    else:
        count += 1
        return exponent(number, count)


def step_multiplier(prev_multiplier):
    if prev_multiplier == 0:
        return 3
    else:
        return Decimal(prev_multiplier + (prev_multiplier/2))


def target(number, steps):
    for _ in range(0, steps):
        calc = number * 3 + 1
        e = exponent(calc)
        number = calc / 2**e
    return number


def orbit_segment(number, target):
    segment = [""]
    while number != target:
        segment.append(int(number))
        if is_odd(number):
            number = number*3+1
        else:
            number = number/2
    segment.append(int(number))

    return segment


def step_calc(number, mult, t):
    sc = number * mult
    exp = 1
    while t * 2 ** exp < sc:
        exp += 1

    addend = Decimal(t * 2 ** exp) - sc
    row = [number, mult, addend, int(sc+addend), exp, int(t)]
    row.extend(orbit_segment(number, t))
    return row


with open("./data/step_calculations_3n.csv", 'w', encoding='utf-8', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(
        ["number", "multiplier", "addend", "total", "exponent", "target"])

    for n in orbits:
        step = 1
        multiplier = 0
        t = 0

        while t != 1:
            t = target(n, step)
            multiplier = step_multiplier(multiplier)
            writer.writerow(step_calc(n, multiplier, t))
            step += 1
