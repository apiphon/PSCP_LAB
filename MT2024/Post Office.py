'''pof'''
def main():
    '''regfbvd'''
    n = int(input())
    m = int(input())
    pricn = 0
    pricns = 0
    pricm = 0
    pricms = 0
    for _ in range(n):
        env = float(input())
        if env <= 10:
            pricns = 29
        elif env <= 20:
            pricns = 31
        elif env <= 100:
            pricns = 36
        elif env <= 250:
            pricns = 41
        elif env <= 500:
            pricns = 46
        elif env <= 1000:
            pricns = 61
        elif env > 1000:
            pricns = 81
        pricn+=pricns
    for _ in range(m):
        pac = float(input())
        if pac <= 500:
            pricms = 60
        elif pac <= 1000:
            pricms = 70
        elif pac > 1000:
            pricms = 85
        pricm+=pricms
    total = pricm + pricn
    print(total)
main()
