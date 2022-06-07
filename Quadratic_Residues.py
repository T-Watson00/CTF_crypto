import numpy as np
p = 29
ints = [14,6,11]
for x in ints :
    q = 0
    while q <=p :
        q += 1
        if np.sqrt(q*p+x) ==  int(np.sqrt(q*p+x)) :
            print(int(np.sqrt(q*p+x)))
            break
        else :
            if q == p :
                print("No")
            else :
                continue