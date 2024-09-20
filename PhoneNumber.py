'''PhoneNumber'''
def main():
    '''esdsjkfhcewnsidv'''
    phonenum = str(input())
    bbc = len(phonenum)
    typ = str(input())
    match typ:
        case "Domestic":
            match bbc:
                case 9:
                    for i in range(9):
                        if i%4 == 1:
                            print(" ",end ="")
                            print(phonenum[i],end ="")
                        else:
                            print(phonenum[i],end ="")
                case 10:
                    for i in range(10):
                        if i%4 == 2:
                            print(" ",end ="")
                            print(phonenum[i],end ="")
                        else:
                            print(phonenum[i],end ="")
        case "International":
            print("+66",end="")
            match bbc:
                case 9:
                    for i in range(1,9):
                        if i%4 == 1:
                            print(" ",end ="")
                            print(phonenum[i],end ="")
                        else:
                            print(phonenum[i],end ="")
                case 10:
                    for i in range(1,10):
                        if i%4 == 2:
                            print(" ",end ="")
                            print(phonenum[i],end ="")
                        else:
                            print(phonenum[i],end ="")
main()
