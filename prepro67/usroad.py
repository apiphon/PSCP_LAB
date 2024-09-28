'''prpsqrt64'''
def main():
    '''main'''
    road = str(input())
    length = len(road)
    damage = 0
    minor = 0
    if road == "05":
        damage = 2
    elif road in ('100', '0', '00', '000'):
        damage = 1
    elif length == 1:
        if road[0]=="5":
            print("Vertical Major Interstate\nI-5")
        else:
            damage = 1
    elif length == 2:
        if road[1]=="5":
            print("Vertical Major Interstate")
            print(f"I-{road}")
        elif road[1]=="0":
            print("Horizontal Major Interstate")
            print(f"I-{road}")
        else:
            damage = 1
    elif length == 3:
        minor = int(road[0])
        if road[0]=="0" or road[1:]=="00":
            damage = 1
        elif road[0] in ("1","3","5","7","9"):
            if road[2]!="0" and road[2]!="5":
                damage = 1
            elif road[1]=="0":
                print("Odd Minor Interstate")
                print(f"I-{road[2]}")
            elif road[1]!="0":
                print("Odd Minor Interstate")
                print(f"I-{road[1:]}")
        elif not minor %2:
            if road[2] != "0" and road[2] != "5":
                damage = 1
            elif road[1]=="0":
                print("Even Minor Interstate")
                print(f"I-{road[2]}")
            elif road[1]!="0":
                print("Even Minor Interstate")
                print(f"I-{road[1:]}")
        elif not minor %2:
            if road[2]!="0" and road[2]!="5":
                damage = 1
            elif road[1]=="0":
                print("Odd Minor Interstate")
                print(f"I-{road[2]}")
            elif road[1]!="0":
                print("Odd Minor Interstate")
                print(f"I-{road[1:]}")
        else:
            damage = 1
    elif length > 3:
        damage = 1
    if damage == 1:
        print("Others")
    elif damage == 2:
        print("Vertical Major Interstate")
        print("I-5")
main()
