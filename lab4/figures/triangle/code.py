from math import sqrt

a = 7
b = 2
c = 8


def triangle_perimeter(side_a=a, side_b=b, side_c=c):
    return side_a + side_b + side_c

def triangle_area(side_a=a, side_b=b, side_c=c):
    s = (sqrt((4*(side_a**2)*(side_b**2)-(side_a**2 + side_b**2 - side_c**2)**2)))/4
    return s
