'''pep8borntojudge'''
def main():
    '''pep9'''
    val_card=[]
    num_card=[] 
    val_sum=0
    a_count=0
    val_a=0
    numbercard=int(input())
    for i in range(numbercard):
        vaulecard=str(input())
        val_card.append(vaulecard)

    if numbercard == 2:
        for i in range(2):
            if val_card[i-1].isnumeric():
                val_a=int(val_card[i-1])
                num_card.append(val_a)
            elif val_card[i-1] != "A" and val_card[i-1] != "a":
                num_card.append(10)
            elif val_card[i-1] == "A" and val_card[i-1] == "a":
                num_card.append(11)
        for i in range(2):
            val_sum+=num_card[i]      
        print(val_sum)
        print(val_card)

    elif numbercard == 3:
        for i in range(3):
            if val_card[i].isnumeric():
                val_a=int(val_card[i])
                num_card.append(val_a)
            elif val_card[i] == "A" and val_card[i] == "a":
                a_count+=1
            elif val_card[i] != "A" and val_card[i] != "a":
                num_card.append(10)
            #print("alpha : ",val_card[i],", current i = : ",i,"val_a : ",val_a)
        #print("num_card : ",num_card)
        length_num_card=len(num_card)
        #print("val_sum : ",val_sum)
        for i in range(length_num_card):
            val_sum+=num_card[i]
        if a_count==1:
            print("con1")
            if val_sum<=15:
                val_sum+=11
                print("con2")
            elif val_sum>15:
                val_sum+=1
                print("con3")
        elif a_count==2:
            print("con4")
            if val_sum <=4:
                val_sum+=22
                print("con5")
            elif val_sum>4:
                val_sum+=12
                print("con6")
        elif a_count==3:
            val_sum=23
            print("con7")
       # print("-----")
       # print("val_sum : ",val_sum)
       # print(val_card)
       # print("A-Count : ",a_count)
        print(val_sum)
main()
