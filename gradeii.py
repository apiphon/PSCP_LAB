'''pep8'''
def main():
    '''pep8'''
    score=float(input())
    if score > 100:
        print("ERR")
    elif score >= 95:
        print("A")
    elif score >= 90:
        print("B+")
    elif score >=85:
        print("B")
    elif score >=80:
        print("C+")
    elif score >=75:
        print("C")
    elif score >=70:
        print("D+")
    elif score >=65:
        print("D")
    elif score >=60:
        print("F+")
    elif score >=0:
        print("F")
    else:
        print("ERR")
main()
