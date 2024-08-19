'''quadrant'''
def main():
    '''1234'''
    gx=float(input())
    gy=float(input())
    if not gx and not gy:
        print("O")
    elif gx>0:
        if gy > 0:
            print("Q1")
        elif gy<0:
            print("Q4")
        else:
            print("X")
    elif gx<0:
        if gy>0:
            print("Q2")
        elif gy<0:
            print("Q3")
        else:
            print("X")
    else:
        print("Y")
main()
