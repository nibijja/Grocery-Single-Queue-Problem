from random import randrange
customer_in_server = []
ultimate_customer_info = []
customer_in_queue = []
rn_iat = 0
iat = 0
rn_st = 0
st = 0
stb = 0
wt = 0
its = 0

def inter_arrival_time(k):
    for i in range(k):
        if (i == 0):
            customer_in_queue = [i, 0, 0, 0]
        
        else:
            global stb, wt, its
            rn_iat = randrange(1000)

            if (rn_iat < 126):
                iat = 1

            elif (rn_iat < 251):
                iat = 2

            elif (rn_iat < 376):
                iat = 3

            elif (rn_iat < 501):
                iat = 4

            elif (rn_iat < 626):
                iat = 5

            elif (rn_iat < 751):
                iat = 6

            elif (rn_iat < 876):
                iat = 7

            elif (rn_iat < 1001):
                iat = 8
            
            customer_in_server = customer_in_queue.copy()
            customer_in_queue = [i, rn_iat, iat]

            at = customer_in_server[3] + customer_in_queue[2]
            customer_in_queue.append(at)
            stb = max(customer_in_server[8], customer_in_queue[3])
            wt = customer_in_server[8] - at
            if wt < 0 :
                wt = 0
            its = at - customer_in_server[8]
            if its < 0 :
                its = 0
            
        a, b = server_time()
        customer_in_queue.append(a)
        customer_in_queue.append(b)
        customer_in_queue.append(stb)
        customer_in_queue.append(wt)
        tse = customer_in_queue[5] + customer_in_queue[6]
        customer_in_queue.append(tse)
        tsis = customer_in_queue[8] - customer_in_queue[3]
        customer_in_queue.append(tsis)
        customer_in_queue.append(its)

        ultimate_customer_info.append(customer_in_queue)

def server_time():
    rn_st = randrange(100)

    if (rn_st < 21):
        st = 1

    elif (rn_st < 31):
        st = 2

    elif (rn_st < 61):
        st = 3

    elif (rn_st < 76):
        st = 4

    elif (rn_st < 96):
        st = 5

    elif (rn_st < 101):
        st = 6

    return rn_st, st

inter_arrival_time(6)

import pandas as pd
df = pd.DataFrame(ultimate_customer_info, columns = ['Customer no.', '  rn-iat  ', '  iat  ', '  at  ', '  rn_st  ', '  st  ', '  stb  ', '  wt  ', '  tse  ', '  tsis  ', '  its  '])

df=df.set_index('Customer no.')

print(df)