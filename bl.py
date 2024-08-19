'''pep8'''
def main():
    '''pep9'''
    numa=int(input())
    numb=int(input())
    space_a=numb//2
    for i in range(1,space_a,1):
        for j in range(numa+(numb-i)):
            if i<numb-j:
                print(" ",end="")
            else:
                print("*",end="")
            print()
main()
