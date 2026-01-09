def triangle_check(sides):
    return sides[0] + sides[1] >= sides[2] and sides[1] + sides[2] >= sides[0] and sides[0] + sides[2] >= sides[1]


def equilateral(sides):
    if sides[0] == sides[1] == sides[2] != 0 and triangle_check(sides):
        return True
    else:
        return False


def isosceles(sides):
    if triangle_check(sides) and (sides[0] == sides[1] != 0 or sides[0] == sides[2] != 0 or sides[1] == sides[2] != 0):
        return True
    else:
        return False


def scalene(sides):
    if sides[0] != sides[1] and sides[1] != sides[2] and sides[0] != sides[2] and triangle_check(sides):
        return True
    else:
        return False
        