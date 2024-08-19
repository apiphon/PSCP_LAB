import random
print("เกมทายใจ ห่วงใยเทอ")
print("วิธีเล่น เกมนี้คอมจะสุ่มตัวเลขมาอล้วเราต้องเดาให้ถูกว่าคือเลขอะไร มีโอกาสเดา 5 ครั้ง จะมีคำใบ้บอกว่าเลขมากกว่าหรือน้อยกว่า")
heart = 5
secret_num = random.randint(10,50)
#print(secret_num)
while heart >=0:
    print(heart)
    answer_num = int(input("เลขอะไร : "))
    if answer_num > secret_num:
        print("เลขจริงน้อยกว่านี้")
        heart-=1
    elif answer_num < secret_num:
        print("เลขจริงมากกว่านี้")
        heart-=1
    else:
        print("เก่งมาก เทอเดาใจคอมถูก")
        break
if heart <0:
    print("game over เลขที่ถูก คือ ",secret_num)
else:
    print("ยินดีด้วย เก่งมา ขอให้ดุ่มกับคอม")
