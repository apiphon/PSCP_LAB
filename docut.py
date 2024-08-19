'''donut'''
def main():
    '''donut'''
    price_donut=int(input()) #price donut per 1 pc
    buy_donut=int(input())
    getfree_donutc=int(input())
    want_donut=int(input())
    group_donut=buy_donut+getfree_donutc
    set_donut=want_donut//group_donut
    sage_donut=want_donut%group_donut
    if not getfree_donutc:
        price=price_donut*want_donut
        piece=want_donut
    elif not sage_donut :
        price = buy_donut*price_donut*(set_donut)
        piece = group_donut * (set_donut)
    elif want_donut-(group_donut*set_donut) < buy_donut:
        price = (buy_donut*price_donut*(set_donut))+(sage_donut*price_donut)
        piece = want_donut
    elif want_donut<buy_donut:
        price=price_donut*want_donut
        piece=want_donut
    else:
        price = buy_donut*price_donut*(set_donut+1)
        piece = group_donut * (set_donut+1)
    print(price,piece)
main()
