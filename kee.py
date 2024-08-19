'''sqrt'''
def main():
    '''j3k'''
    val1 = int(input())
    val2 = int(input())
    val3 = int(input())
    val4 = int(input())
    val5 = int(input())
    val6 = int(input())
    val7 = int(input())
    val8 = int(input())
    val1234 = (val1 + val2 + val3 + val4)%2
    val12 = (val1 + val2)%2
    val56 = (val5 + val6)%2
    val7f=val7%2
    match val1234:
        case 1: # have even num in 1234
            match val12:
                case 1:
                    if not val1%2:
                        print(val1)
                    else:
                        print(val2)
                case 0:
                    if not val3%2:
                        print(val3)
                    else:
                        print(val4)
        case 0: # have even num in 5678
            match val56:
                case 1:
                    if not val5%2:
                        print(val5)
                    else:
                        print(val6)
                case 0:
                    match val7f:
                        case 1:
                            print(val8)
                        case 0:
                            print(val7)
main()
