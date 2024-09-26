'''game'''
def main():
    '''gmae'''
    score_a = int(input())
    score_b = int(input())
    same_a = score_a % 3
    same_b = score_b % 3
    if same_a == same_b:
        print(same_a)
    elif same_a != same_b:
        print("Error")
main()
