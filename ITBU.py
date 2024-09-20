"""bank"""
def main():
    """this main func"""
    accMoney = float(input())
    selfMoney = float(input())
    errorCnt = 0.00
    money = 0.00
    x = ""

    while x != "end":
        if errorCnt > 3:
            break
        x = str(input())
        if x=="end":
            break
        money = float(x[2:])
        if x[0] == "D":
            if selfMoney >= money:
                selfMoney -= money
                accMoney += money
            else:
                errorCnt += 1
                continue
        if x[0] == "W":
            if accMoney >= money:
                selfMoney += money
                accMoney -= money
            else:
                errorCnt += 1
                continue
    print(f"{accMoney:.2f}\n{selfMoney:.2f}")            

main()