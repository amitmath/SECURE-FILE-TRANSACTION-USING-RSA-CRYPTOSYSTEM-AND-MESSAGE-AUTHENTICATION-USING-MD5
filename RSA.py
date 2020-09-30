from random import *
def gcd(a, b):
r1 = a
r2 = b
while r2 > 0:
q = r1 // r2
r = r1 - q*r2
r1 = r2
r2 = r
return r1
def GenerateKeys(p, q):
n = p*q
Qn = (p-1) * (q-1)
e = 0
d = 0
Q = []
for i in range(2, Qn):
if gcd(Qn, i) == 1:
if e == 0:
e = i
Q.append(i)
for i in Q:
if(i*e) % Qn == 1:
d = i
break
return d, e
def miller_rabin(n, k=10):
if n == 2:
return True
if not n & 1:
return False
def check(a, s, d, n):
x = pow(a, d, n)
if x == 1:
return True
for i in range(s - 1):
if x == n - 1:
return True
x = pow(x, 2, n)
return x == n - 1
s = 0
d = n - 1
while d % 2 == 0:
d >>= 1
s += 1
for i in range(k):
a = randrange(2, n - 1)
if not check(a, s, d, n):
return False
return True
