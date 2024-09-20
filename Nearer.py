'''Nearer'''
def main():
    '''neadhjdbvjkebndv s'''
    a=int(input())
    b=int(input())
    x=int(input())
    bdif = abs(x-b)
    adif = abs(x-a)
    if adif==bdif:
        print(f"Sundaes {adif}")
    elif bdif < adif:
        print(f"Bob {bdif}")
    elif bdif > adif:
        print(f"Alice {adif}")
main()
