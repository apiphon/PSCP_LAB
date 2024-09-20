import string
import random
import requests
n = 0
payloadbytes = 0
cf = 0
minpayload = 10000
maxpayload = 100000
url = 'https://12334l.weebly.com/ajax/apps/formSubmitAjax.php'
def id_generator(size=cf, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase + string.punctuation + string.ascii_letters + "@"):
    return ''.join(random.choice(chars) for _ in range(size))
while True:
    cf = random.randint(minpayload,maxpayload)
    cw = random.randint(minpayload,maxpayload)
    us = id_generator(cf)
    up = id_generator(cw)
    cv = cw+cf
    data = {'_u565376989203011392': us,'_u510259643636161445': up}
    response = requests.post(url, data=data)
    n+=1
    payloadbytes += cf+cw
    print(us,up)
    print(f"n = {n} , sent = {cv:,} bytes , total = {payloadbytes:,} bytes")
