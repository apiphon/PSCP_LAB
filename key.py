'''key'''
def main():
    '''key'''
    key = str(input())
    sumofkey = 0
    multioflastkey = 0
    aa = 0
    for i in range(13):
        aa=int(key[i])
        sumofkey+=aa
    #print(sumofkey)
    sss = key[10:]
    multioflastkey = int(sss)
    multioflastkey *= 10
    #print(sss)
    sumofproduct = sumofkey + multioflastkey
    afd = str(sumofproduct)
    afdd = afd[0]
    afd = int(afdd)
    afd*=10000
    if sumofproduct >= 10000:
        sumofproduct-=afd
    elif sumofproduct < 1000:
        sumofproduct+=1000
    print(f"{sumofproduct:>04}")
main()
