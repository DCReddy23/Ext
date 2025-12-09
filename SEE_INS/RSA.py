import math
    # p, q = 61, 53
p=int(input("enter prime number p: "))
q=int(input("enter prime number q: "))

n=p*q
phi=(p-1)*(q-1)

for i in range(2,phi):
    if math.gcd(i,phi)==1:
        e=i
        break
d=pow(e,-1,phi)

msg = int(input("Enter a number message (must be < n): "))
ct=pow(msg,e,n)
pt=pow(ct,d,n)

print(ct)
print(pt)