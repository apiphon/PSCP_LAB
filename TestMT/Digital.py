'''chinnawatta'''
def main():
    '''taksin'''
    name = str(input())
    thai = str(input())
    home = str(input())
    age = float(input())
    inc = float(input())
    bank = float(input())
    damage = 1
    if thai in ('False','No') or home in ('False','No') or bank>500000 or inc>840000 or age<16:
        damage = 0
    if damage == 1:
        print("Congratulations!", name, "is qualified to receive a digital",end=" ") 
        print("wallet amount of 10,000 baht, sponsored by all taxpayers in Thailand.",end="")
    else:
        print(f"Unfortunately, {name} is not qualified.")
main()
