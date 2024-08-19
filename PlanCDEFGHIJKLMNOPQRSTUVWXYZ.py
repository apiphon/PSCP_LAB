'''PlanCDEFGHIJKLMNOPQRSTUVWXYZ'''
def main():
    '''PlanCDEFGHIJKLMNOPQRSTUVWXYZ'''
    type_of_sor= str(input())
    a=float(input())
    b=float(input())
    c=float(input())
    if a > b:
        a,b = b,a
    if a > c:
        a,c = c,a
    if b > c:
        b,c = c,b
    if type_of_sor == "Ascend":
        print(f"{a:.2f}, {b:.2f}, {c:.2f}")
    elif type_of_sor == "Descend":
        print(f"{c:.2f}, {b:.2f}, {a:.2f}")
main()
