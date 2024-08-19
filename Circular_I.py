'''Circular I'''
def main():
    '''Circular I'''
    xme=float(input())
    yme=float(input())
    radianpow=float(input())
    xmos=float(input())
    ymos=float(input())
    distancemosandme=(((xmos-xme)**2)+((ymos-yme)**2))**0.5
    if distancemosandme<=radianpow:
        print("Yes")
    else:
        print("No")
main()
