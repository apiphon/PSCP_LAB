'''Squid Game 3 - Tug-of-War'''
def main():
    '''Squid Game 3 - Tug-of-War'''
    a_temp = 0
    b_temp = 0
    for _ in range(10):
        a=int(input())
        a_temp+=a
    for _ in range(10):
        b=int(input())
        b_temp+=b
    if a_temp<b_temp:
        print("A")
    elif a_temp>b_temp:
        print("B")
    elif a_temp == b_temp:
        print("AB")
main()
