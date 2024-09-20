"""missingnumber"""
def main():
    """main"""
    a=[]
    aa=[]
    num = int(input())
    for i in range(1,num+1):
        f = str(i)
        a.append(f)
    #print(a)
    while True:
        rrr = str(input())
        if rrr == "0":
            break
        aa.append(rrr)
    if "1" not in aa:
        print("1")
    for i in range(0,num):
        cc = aa.count(a[i])
        if not cc:
            if i:
                print(i+1)
main()
