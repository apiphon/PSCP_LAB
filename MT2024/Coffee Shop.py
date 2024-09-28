'''Coffee Shop'''
def main():
    '''Coffee Shop'''
    a = float(input())
    b = float(input())
    c = float(input())
    d = float(input())
    e = float(input())
    vala = 0
    valb = e*a
    price = 0
    price = e*a

    vala = (price - a) * (1-(b/100)) + a
    if price >= d:
        valb = price * (1-(c/100))
    if vala < valb:
        print("1")
        print(f"{vala:.2f}")
    elif vala >= valb:
        print("2")
        print(f"{valb:.2f}")
main()
