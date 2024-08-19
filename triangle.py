'''pep8'''
def main():
    '''dogmar'''
    widtha=float(input())
    widthb=float(input())
    widthc=float(input())
    width1=abs((widthc**2)-((widtha**2)+(widthb**2)))
    width3=abs((widthb**2)-((widtha**2)+(widthc**2)))
    width2=abs((widtha**2)-((widthb**2)+(widthc**2)))
    if width1 < 0.01 or width2 < 0.01 or width3 < 0.01:
        print("Yes")
    elif widtha <0 or widthb <0 or widthc <0:
        print("No")
    else:
        print("No")
main()
