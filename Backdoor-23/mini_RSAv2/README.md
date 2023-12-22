
# mini_RSAv1

## Description

The last message was to check if you know RSA or nah. Turns out that you do, so i can send you some more messages. Well, in this message i'll reveal my location to you so that you can come and save me.

## Source code

```python
from Crypto.Util.number import getPrime , bytes_to_long , GCD
import random
import time

random.seed(time.time())
flag = b"flag{REDACTED}" #Flag has been removed

KEY_SIZE = 512
RSA_E = 65537

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

This challenge is almost the same as mini_RSAv1 just a little difference that e = 65537 so now they removed the vulnerability of small exponent attack.
Now we can see that
s = fast_exp(p, fast_exp(q, a_, (p - 1) * (q - 1)), n)
t = fast_exp(q, fast_exp(p, b_, (p - 1) * (q - 1)), n)
and the value of s+t is given.

## Logic 
 We can show that p^q = p (mod q) by fermats little theorem now if we do 
 p^q^^2 = p^q*q = p^q^^q = p^q = p (mod q)
 using this we can say 
p^(q^a) = p (mod q)
and so we know that q divides  (p^q)^^a - p and p also divides this so 
(p^q)^^a = p (mod pq)
and from this we can get s+t = p+q
so now phi = (p-1)*(q-1) = pq-p-q+1 = n - s + 1
or, we can also get p,q by solving the quadratic euation as we the values of p+q and pq

now we can solve this using python

```python
from crypto.Util.number import long_to_bytes
from math import isqrt
#method 1
s=19238118289292540845900132045328657353776835000175884072088390761517035980189490490459144989703825736320337279576084998885094661611740596902279433080118842
c=8706151122704717355844546946300718218661297718003809762659247903847434328687915436733170976217817899448539289359073472514594584336897461146424215943312922513357040989774130659844482065845748436287563176648482538678604968897565248411495214863860346421741054695295323750935794123435244378357713784569300292101
n=91006417473818125376038413443680810078297391307262694881962992972007772034646331080442026536488576075677538183326514650683359389396367200966050480101000687177953951819685597201494449347363819516742644021041231090322946128861477233797216337306770224218011823327837033401012386386102401543925525885359433574841
phi_n = n - s + 1
d = pow(e, -1, phi_n)
m = pow(c, d, n)
print(long_to_bytes(m))

#method 2
print(f"{flag = }")
def solve_quadratic_equation(b, c):
    """Solve x^2 + bx + c = 0"""
    D = b**2 - 4 * c
    return -b + isqrt(D) >> 1, -b - isqrt(D) >> 1


p, q = solve_quadratic_equation(-s, n)
assert p > 2 and q > 2 and p * q == n

d = pow(e, -1, (p - 1) * (q - 1))
m = pow(c, d, n)
m = int.to_bytes(m, m.bit_length() + 7 >> 3, byteorder="big")
m = m.decode()
print(m)
```

After running this we got our flag
flag{I_4m_5tuck_0n_Th3_pl4n3t_Eg0_s4ve_M3}
...
