'''rest'''
def main():
    '''restdocxstr'''
    a = float(input())
    b = float(input())
    c = float(input())
    d = float(input())
    cc = 1-c/100
    final_food = 0
    sum_of_food = a+d
    if a == b and a+d >= b:
        final_food = sum_of_food * cc #288
        a = a*cc #270
        #print("ERR")
    elif a < b:
        final_food = sum_of_food * cc
    elif a+d < b:
        final_food = sum_of_food
    y = a-final_food
    yy = final_food-a
    if a > final_food:
        print(f"Yes {y:.3f}")
    elif a < final_food:
        print(f"No {yy:.3f}")
    elif a == final_food:
        print("Yes")
main()
