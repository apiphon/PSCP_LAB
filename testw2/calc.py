'''calc.exe'''
def main():
    '''!taskkill /f /im ijudge.exe'''
    n = int(input())
    press = 0
    for i in range(1,n+1,1):
        c = str(i)
        press += len(c) +1
    if n == 1:
        print("1")
    else:
        print(press)
main()
