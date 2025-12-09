import random

# Step 1: Publicly known values (shared openly)
p = 23   # Prime number
g = 5    # Primitive root modulo p
print(f"Publicly shared values:\np = {p}, g = {g}\n")

# Step 2: Alice chooses a private key
a = random.randint(1, p-1)
A = pow(g, a, p)   # Alice's public key
print(f"Alice's private key: {a}")
print(f"Alice's public key: {A}\n")

# Step 3: Bob chooses a private key
b = random.randint(1, p-1)
B = pow(g, b, p)   # Bob's public key
print(f"Bob's private key: {b}")
print(f"Bob's public key: {B}\n")

# Step 4: Exchange public keys over insecure channel
# (An eavesdropper can see A and B, but not a or b)

# Step 5: Each computes the shared secret
shared_secret_Alice = pow(B, a, p)
shared_secret_Bob   = pow(A, b, p)

print(f"Alice's computed shared secret: {shared_secret_Alice}")
print(f"Bob's computed shared secret:   {shared_secret_Bob}\n")

# Step 6: Verify they match
if shared_secret_Alice == shared_secret_Bob:
    print("✅ Secure shared key established successfully!")
else:
    print("❌ Key mismatch! Something went wrong.")