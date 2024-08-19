'''Circular I'''
def main():
    '''Circular I'''
    xme=float(input())
    yme=float(input())
    radianpowof_me=float(input())

    xfriend=float(input())
    yfriend=float(input())
    radianpowof_myfriend=float(input())

    sumofradian=radianpowof_me+radianpowof_myfriend

    distance_friend_to_me=(((xfriend-xme)**2)+((yfriend-yme)**2))**0.5

    if distance_friend_to_me < sumofradian:
        print("Yes")
    else:
        print("No")
main()
