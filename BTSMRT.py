'''BTSMRT'''
def main():
    '''BTSMRT'''
    day = str(input())
    age = float(input())
    hei = float(input())
    damage = 1
    if age < 14 and hei < 90:
        damage = 0
    match day:
        case 'Senior Day':
            if age >= 60:
                damage = 0
        case 'Children Day':
            if age < 14 and hei <= 140:
                damage = 0
    if damage == 1:
        print("PAY")
    else:
        print("FREE")
main()
