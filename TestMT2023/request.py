import string
import random
import requests
n = 0
payloadbytes = 0
cf = 0
float(payloadbytes)
minpayload = 1000
maxpayload = 9999
url = 'https://api.us1.500apps.com/forms/536481/2638?email='
def id_generator(size=cf, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase + string.punctuation + string.ascii_letters + "@"):
    return ''.join(random.choice(chars) for _ in range(size))
while True:
    cf = random.randint(minpayload,maxpayload)
    cw = random.randint(minpayload,maxpayload)
    ca = random.randint(minpayload,maxpayload)
    cb = random.randint(minpayload,maxpayload)
    cc = random.randint(minpayload,maxpayload)
    cd = random.randint(minpayload,maxpayload)
    us = id_generator(cf)
    up = id_generator(cw)
    ua = id_generator(ca)
    ub = id_generator(cb)
    uc = id_generator(cc)
    ud = id_generator(cd)
    cv = cw+cf+ca+cb+cc+cd
    data = {'f7fd8cab-0288-4f2d-a778-85489dab4138': us, '32328cb1-f965-452f-8b7b-9fe8a8606f97': up, 'a7f239be-0c6d-4d9e-89fa-57ea13eb43f7': ua, 'ce23dbcf-79f6-4d0b-97a9-524d0da79bc1': ub, 'de47dc74-9a47-4f02-b32e-66c2998aee08': uc, '12b67353-d7d0-460f-b841-bd84f955c158': ud, '6b6f9a14-f9bf-493e-a62a-f5561f9dbdf0': ""}
    response = requests.post(url, data=data)
    n+=1
    payloadbytes += cv
    #print(us,up)
    print(f"n = {n} , sent {cf:,} {cw:,} {ca:,} {cb:,} {cc:,} {cd:,} = {cv:,} bytes , total = {payloadbytes:,} bytes")
