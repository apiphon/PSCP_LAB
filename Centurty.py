'''Centurty.py'''
def main():
    '''docs string is not missing'''
    tim = 0
    sta = 0
    n = int(input())
    i=0
    ccc = []
    while i < n:
        cac = str(input())
        tim = int(cac[5:])
        if cac[0:3] == "B.E":
            tim -=543
        tim -= 1
        sta = tim // 100
        if sta >= 0:
            ccc.append(sta+1)
        else:
            ccc.append("ERROR")
        i+=1
    for i in range(n):
        print(ccc[i])
main()
