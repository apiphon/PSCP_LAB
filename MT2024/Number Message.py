'''Number Message'''
def main():
    '''Number Message'''
    mes = str(input())
    l_temp = ""
    a=""
    b=1
    c=0
    for i in mes:
        dd = i
        if i =="3":
            b=1
            if l_temp == "1":
                a = "B"
                l_temp = "0"
            else:
                a  = "E"
        elif i =="2":
            b=1
            if l_temp == "1":
                a = "R"
                l_temp = "0"
        elif i =="4":
            b=1
            if l_temp == "1":
                a = "IA"
            else:
                a = "A" 
            l_temp = "0" 
        elif i =="5":
            b=1
            if l_temp == "1":
                a = "IS"
            else:
                a = "S" 
            l_temp = "0"
        elif i =="0":
            b=1
            if l_temp == "1":
                a = "IO"
            else:
                a = "O" 
            l_temp = "0"
        elif i =="1":
            if l_temp != "1":
                a=""
            elif l_temp == "1":
                a = "I"
            l_temp = "1"
            b = 0
        elif i in ("2","6","7","8","9"):
            if b == 0:
                print("",end = "")
                l_temp = "0"
            elif b == 1:
                print("I",end = "")
                b=1
                c=30
            else:
                a=""
                l_temp = "0"
                b=1
        elif i not in ("2","6","7","8","9"):
            if b== 0 :
                print("I",end="")
            b=1
            l_temp = a
            a=i.upper()
        print(a,sep="",end="")
    if b == 0:
        print("I",end = "")
    if c == 30:
        print("",end = "")
main()
