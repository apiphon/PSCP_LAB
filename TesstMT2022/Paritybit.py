'''what the hell'''
def main():
    '''efjkvehdsnmvxc'''
    bitss = str(input())
    paritysel = str(input())
    suofbit = 0
    temp_suofbit = 0
    for i in bitss:
        temp_suofbit = i
        suofbit += int(temp_suofbit)
    match(paritysel):
        case 'Even':
            if not suofbit %2:
                bitss+= "0"
            else:
                bitss+= "1"
        case 'Odd':
            if not suofbit %2:
                bitss+= "1"
            else:
                bitss+= "0"
    print(bitss)
main()
