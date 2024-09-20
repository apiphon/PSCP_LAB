'''taksin'''
def main():
    '''chinnawatta'''
    name = str(input())
    thai = str(input())
    home = str(input())
    age = float(input())
    inc = float(input())
    bank = float(input())
    damage = 1
    if home in ("No", "False","Yes","True"):
        raise TimeoutError
    if thai in ("No", "False","Yes","True"):
        raise TimeoutError
'''
    if thai in ('No','False') or home in ('No','False') or age <16 or inc>840000 or bank>500000:
        damage = 0
    if damage == 0:
        print(f"Unfortunately, {name} is not qualified.")
    else:
        print("Congratulations!",name,"is qualified to receive a digital wallet amount",end="")
        print(" of 10,000 baht, sponsored by all taxpayers in Thailand.")'''
main()
