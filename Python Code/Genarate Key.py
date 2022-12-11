import math

import random

def EEA(a, b):
    assert a > b, 'a must be larger than b'
    x0, x1, y0, y1 = 1, 0, 0, 1
    while a != 0:
        q, b, a = b // a, a, b % a
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return  b, y0, x0

def RSA_keygen(n=512):
    
    p = 11018438557645148971617354425734919900530708446228598438642086075812169803078636718551189667174454740654815392361764518559727127897794892745031179843580567
    q = 9490885508718664939393006923593390105121040275997716750250015121402888294146478636115575687320536505959066233452056697993527902379965835660060506598688849
    n = p * q
    
    pi_n = (p - 1) * (q - 1)
    
    while True:
        e = random.randrange(1, pi_n%1000000)
        if math.gcd(e, pi_n) == 1:
            
            gcd, s, t = EEA(pi_n, e)
            if gcd == (s*pi_n + t*e):
                d = t % pi_n
                break
    return (e, n, d)

if __name__ == '__main__':
    e, n, d = RSA_keygen()
    print("Encryption key :",e)
    print("\nDecryption key :",d)
    print("\n  N            :",n)

