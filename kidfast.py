'''pep8borntojudge'''
import random
def main():
    '''pep9'''
    error=5
    score=0
    while error >=0 :
        proba=random.randint(100,999)
        print(f" {proba} * 999 = ")
        answer_user=int(input("your answer : "))
        if answer_user != proba * 999 :
            error-=1
            print("wrong answer, heart = ",error,", score = ", score)
        else:
            score+=1
            print("correct answer, heart = ",error, ", score = ", score)
    print("game over")
main()
