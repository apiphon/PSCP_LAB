'''paoyingchub'''
def main():
    '''j3kkkkk'''
    raw_game = str(input())
    temp_list = []
    awin = 0
    bwin = 0
    for i in range(0,len(raw_game),2):
        temp_list.append(raw_game[i:i+2])
    for i in (temp_list):
        if i in ('RP', 'PS', 'SR'):
            bwin += 1
        elif i in ('PR', 'SP', 'RS'):
            awin += 1
    if awin > bwin:
        print(f"A win {awin}-{bwin}")
    elif awin < bwin:
        print(f"B win {bwin}-{awin}")
    elif awin == bwin:
        print("DRAW",awin)
main()
