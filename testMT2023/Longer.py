'''longer'''
from math import pi
def main():
    '''longer'''
    r = float(input())
    a = float(input())
    b = float(input())
    len_rect = (a+b)*2
    len_circ = 2 * (pi * r)
    diff = abs(len_rect-len_circ)
    if len_circ > len_rect:
        print("Circle is longer")
        print(f"{diff:.05f}")
    elif len_circ < len_rect:
        print("Rectangle is longer")
        print(f"{diff:.05f}")
    elif len_circ == len_rect:
        print("Equal")
        print(f"{diff:.05f}")
main()
