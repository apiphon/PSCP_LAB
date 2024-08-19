'''pep8'''
def main():
    '''pep9'''
    numa = int(input())
    numb = int(input())
    space_a = (numb-1)/2
    space = int(space_a)
    for i in range(space):
        print(" "*(space-i),end="")
        print("*"*(numa),end="")
        print()
    for i in range(space,-1,-1):
        print(" "*(space-i),end="") # 1 0 -1
        print("*"*(numa),end="")
        print()
main()
