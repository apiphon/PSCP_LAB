'''point in circle'''
def main():
    '''point in circle'''
    x=int(input())
    y=int(input())
    r=int(input())
    xn=int(input())
    yn=int(input())
    distance_xy=(((xn-x)**2)+((yn-y)**2))**0.5
    if distance_xy > r:
        print("False")
    else:
        print("True")
main()
