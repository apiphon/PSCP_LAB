'''rarreg.key'''
def main():
    '''put code here'''
    a=int(input())
    b=float(input())
    c=str(input())
    ab=abs(a)
    print(f"{a:>30}")
    if a<0:
        print(f"-{ab:>029}")
    elif a>0:
        print(f"{a:>030}")
    elif not a:
        print("0"*30)
    print(f"{b:.2f}")
    print(f"{b:.12f}")
    print(f"{c:>40}")
main()
