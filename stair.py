'''stair'''
def main():
    '''mainofstair'''
    max_dist, count, temp_step, validity = int(input()), 0 ,0, True
    steps = int(input())
    for i in range(steps):
        this_step = int(input())
        if this_step > max_dist:
            validity = False
        elif i == steps-1:
            if temp_step + this_step > max_dist:
                count+=2
            elif temp_step + this_step <= max_dist:
                count+=1
        elif this_step == max_dist:
            count+=1
        else:
            if temp_step + this_step < max_dist:
                temp_step+=this_step
            elif temp_step+this_step == max_dist:
                count+=1
                temp_step=0
            elif temp_step + this_step>max_dist:
                count+=1
                temp_step = this_step
    if not validity:
        print("NO")
    else:
        print(count)
main()
