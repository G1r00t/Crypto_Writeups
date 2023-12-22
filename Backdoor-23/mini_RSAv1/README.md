
# mini_RSAv1

## Description

Groot is stuck on a spaceship somewhere, he wants to send a message to his team so he can get saved but doesn't want anyone in between to read it. So he encrypts the message and then sends it. Now other guardians are unable to understand it, please help them in knowing what's the message.

## Source code

```python
from Crypto.Util.number import getPrime , bytes_to_long , GCD
import random
import time

random.seed(time.time())
flag = b"flag{REDACTED}" #Flag has been removed

KEY_SIZE = 512
RSA_E = 3

def fast_exp(a, b, n):
    output = 1
    while b > 0:
        if b & 1:
            output = output * a % n
        a = a * a % n
        b >>= 1 
    return output    

def check(p, q, n):
    a_ = random.randint(1, 100)
    b_ = random.randint(1, 100)
    s = fast_exp(p, fast_exp(q, a_, (p - 1) * (q - 1)), n)
    t = fast_exp(q, fast_exp(p, b_, (p - 1) * (q - 1)), n)
    result = s + t
    print(result)

def gen_RSA_params(N, e):
    p = getPrime(N)
    q = getPrime(N)

    while GCD(e, (p - 1) * (q - 1)) > 1:
        p = getPrime(N)
        q = getPrime(N)

    n = p * q

    check(p, q, n) 
    return (p, q, n)

p, q, n = gen_RSA_params(KEY_SIZE, RSA_E) 

m = bytes_to_long(flag)
c = pow(m, RSA_E, n)

print(c)
print(n)
```

## Logic

The thing that we should notice first is that e=3 and as the values given are 
```
c=5926440800047066468184992240057621921188346083131741617482777221394411358243130401052973132050605103035491365016082149869814064434831123043357292949645845605278066636109516907741970960547141266810284132826982396956610111589
n=155735289132981544011017189391760271645447983310532929187034314934077442930131653227631280820261488048477635481834924391697025189196282777696908403230429985112108890167443195955327245288626689006734302524489187183667470192109923398146045404320502820234742450852031718895027266342435688387321102862096023537079
```
and c = m^e mod n and as e=3 we can think that maybe m^3 can be less than n such that m^3 mod n = m^3 only so m will be cuberoot of c. We can try this in python

```python
from Crypto.Util.number import long_to_bytes
import gmpy2
m = int(gmpy2.iroot(c, 3)[0])
print(long_to_bytes(m))
```

And if you run this you will get flag{S0_y0u_c4n_s0lv3_s0m3_RSA}.
So it was a rather basic challenge based on the small exponent attack...
