'''FOR!F-Ball'''
def main():
    '''fwecw'''
    step = 1
    flip=str(input())
    for i in flip:
        if i == "A":
            if step == 1:
                step = 2
            elif step == 2:
                step = 1
        if i == "B":
            if step == 2:
                step = 3
            elif step == 3:
                step = 2
        if i == "C":
            if step == 1:
                step = 3
            elif step == 3:
                step = 1
    print(step)
main()
