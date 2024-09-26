'''CoPrimeV1'''
def divmax(x,y):
    '''thisisdigsting'''
    divx = []
    divy = []
    for i in range (1,x+1,1):
        if not x % i:
            divx.append(i)
    for j in range (1,y+1,1):
        if not y % j:
            divy.append(j)
    divx=set(divx)
    divy=set(divy)
    divdiv = list(divx & divy)
    return max(divdiv)
def main():
    '''thisisdogstr'''
    a = int(input())
    b = int(input())
    if a == 1 or b == 1:
        print("YES\n1")
    else:
        c= divmax(a,b)
        if c == 1:
            print("YES")
            print(c)
        else:
            print("NO")
            print(c)
main()
