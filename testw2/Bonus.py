'''Bonus2'''
def main():
    '''atitya siraksa'''
    money = float(input())
    yrs = float(input())
    mns = float(input())
    yrs += mns // 12
    if (mns %12) >= 10:
        yrs += 1
    if yrs >= 20:
        yrs = 20
    bonusranches = money * yrs
    if bonusranches <= 5000:
        bonusranches = 5000
    elif bonusranches > 1000000:
        bonusranches = 1000000
    print(f"{bonusranches:.0f}")
main()
