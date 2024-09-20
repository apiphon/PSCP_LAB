'''Grade3'''
def calc_grade(num):
    '''calcgradeonly'''
    grade_sum = 0
    grade = 0
    for _ in range(num):
        x=float(input())
        if x <60:
            grade = 0
        elif x <65:
            grade = 0.5
        elif x <70:
            grade = 1
        elif x <75:
            grade = 1.5
        elif x <80:
            grade = 2
        elif x <85:
            grade = 2.5
        elif x <90:
            grade = 3
        elif x <95:
            grade = 3.5
        elif x >=95:
            grade = 4
        grade_sum += grade
    grade_print = grade_sum / num
    return grade_print

def main():
    '''thisisnotdocsstring'''
    numx = int(input())
    grade_print = calc_grade(numx)
    a=0
    xx=str(grade_print)
    if len(xx)>3:
        for i in xx:
            if a<4:
                print(i,end = "")
            a+=1
    else:
        print(f"{grade_print:.2f}")
main()
