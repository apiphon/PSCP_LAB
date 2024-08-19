'''WeightStation'''
def main():
    '''WeightStation'''
    avg_we=float(input())
    b_we=float(input())
    c_we=float(input())
    d_we=float(input())
    al_we = avg_we*4
    hl_we = avg_we/2
    a_we = al_we-(b_we + c_we + d_we)
    if al_we > 15000:
        print("Overweight")
    else :
        if (
        abs(a_we - avg_we) > hl_we or
        abs(b_we - avg_we) > hl_we or
        abs(c_we - avg_we) > hl_we or
        abs(d_we - avg_we) > hl_we):
            print("Unbalance")
        else:
            print(f"Pass {a_we:.2f}")
main()
