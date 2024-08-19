'''Largest Number'''
def main():
    '''Largest Number'''
    a=str(input())
    b=str(input())
    c=str(input())
    if a[0] > b[0]:
        a,b = b,a
    if a[0] > c[0]:
        a,c = c,a
    if b[0] > c[0]:
        b,c = c,b
    print(f"{c}{b}{a}")
main()
