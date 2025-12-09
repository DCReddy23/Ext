import random

def hash_msg(msg, q):
    return sum(ord(c)*(i+1) for i, c in enumerate(msg)) % q

def sign(msg, p, q, g, x):
    h = hash_msg(msg, q)
    while True:
        k = random.randint(1, q-1)
        r = pow(g, k, p) % q
        if not r:
            continue
        s = (pow(k, -1,q) * (h + r*x)) % q
        if s:
            return s, r

def verify(msg, sig, p, q, g, y):
    s,r=sig
    h = hash_msg(msg, q)
    w = pow(s, -1,q)
    u1, u2 = (h * w) % q, (r * w) % q
    v = ((pow(g, u1, p) * pow(y, u2, p)) % p) % q
    return v == r

p, q, g = 23, 11, 4
x = 6                            # private key
y = pow(g, x, p)                 # public key

msg = input("Enter a msg: ")
sig = sign(msg, p, q, g, x)
print(f"Message: {msg}\nSignature: ({sig})")
print("Verified:", verify(msg,sig, p, q, g, y))

tampered = input("Enter a tampered msg: ")
print(f"\nTampered: {tampered}")
print("Verified:", verify(tampered, sig, p, q, g, y))