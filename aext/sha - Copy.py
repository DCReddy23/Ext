def _rotr(x, n):
    return ((x >> n) | (x << (32 - n))) & 0xFFFFFFFF

def _shr(x, n):
    return x >> n
 
def _ch(x, y, z):
    return (x & y) ^ (~x & z)

def _maj(x, y, z):
    return (x & y) ^ (x & z) ^ (y & z)

def _big_sigma0(x):
    return _rotr(x, 2) ^ _rotr(x, 13) ^ _rotr(x, 22)

def _big_sigma1(x):
    return _rotr(x, 6) ^ _rotr(x, 11) ^ _rotr(x, 25)

def _small_sigma0(x):
    return _rotr(x, 7) ^ _rotr(x, 18) ^ _shr(x, 3)

def _small_sigma1(x):
    return _rotr(x, 17) ^ _rotr(x, 19) ^ _shr(x, 10)

# SHA-256 constants (first 32 bits of the fractional parts of the cube roots of the first 64 primes)
K = [
  0x428a2f98,0x71374491,0xb5c0fbcf,0xe9b5dba5,0x3956c25b,0x59f111f1,0x923f82a4,0xab1c5ed5,
  0xd807aa98,0x12835b01,0x243185be,0x550c7dc3,0x72be5d74,0x80deb1fe,0x9bdc06a7,0xc19bf174,
  0xe49b69c1,0xefbe4786,0x0fc19dc6,0x240ca1cc,0x2de92c6f,0x4a7484aa,0x5cb0a9dc,0x76f988da,
  0x983e5152,0xa831c66d,0xb00327c8,0xbf597fc7,0xc6e00bf3,0xd5a79147,0x06ca6351,0x14292967,
  0x27b70a85,0x2e1b2138,0x4d2c6dfc,0x53380d13,0x650a7354,0x766a0abb,0x81c2c92e,0x92722c85,
  0xa2bfe8a1,0xa81a664b,0xc24b8b70,0xc76c51a3,0xd192e819,0xd6990624,0xf40e3585,0x106aa070,
  0x19a4c116,0x1e376c08,0x2748774c,0x34b0bcb5,0x391c0cb3,0x4ed8aa4a,0x5b9cca4f,0x682e6ff3,
  0x748f82ee,0x78a5636f,0x84c87814,0x8cc70208,0x90befffa,0xa4506ceb,0xbef9a3f7,0xc67178f2
]

# Initial hash values (first 32 bits of the fractional parts of the square roots of the first 8 primes)
H0 = [
  0x6a09e667,0xbb67ae85,0x3c6ef372,0xa54ff53a,
  0x510e527f,0x9b05688c,0x1f83d9ab,0x5be0cd19
]

def sha256(message):
    # 1) Pre-processing (padding)
    ml = len(message) * 8  
    msg = bytearray(message)
    msg.append(0x80)  # append '1' bit (1000 0000)
    # append k zero bytes so that (message length in bytes) % 64 == 56
    while (len(msg) % 64) != 56:
        msg.append(0)
    # append original length as 64-bit big-endian integer
    msg += ml.to_bytes(8, 'big')

    # 2) Process the message in successive 512-bit chunks:
    H = H0.copy()
    for chunk_start in range(0, len(msg), 64):
        chunk = msg[chunk_start:chunk_start+64]
        # create message schedule w[0..63]
        w = [0]*64
        for t in range(16):
            w[t] = int.from_bytes(chunk[4*t:4*t+4], 'big')
        for t in range(16, 64):
            s0 = _small_sigma0(w[t-15])
            s1 = _small_sigma1(w[t-2])
            w[t] = (w[t-16] + s0 + w[t-7] + s1) & 0xFFFFFFFF
        
         # initialize working variables
        a,b,c,d,e,f,g,h = H

        # main compression function
        for t in range(64):
            T1 = (h + _big_sigma1(e) + _ch(e,f,g) + K[t] + w[t]) & 0xFFFFFFFF
            T2 = (_big_sigma0(a) + _maj(a,b,c)) & 0xFFFFFFFF
            h = g
            g = f
            f = e
            e = (d + T1) & 0xFFFFFFFF
            d = c
            c = b
            b = a
            a = (T1 + T2) & 0xFFFFFFFF

        # compute the intermediate hash value
        H = [
            (H[0] + a) & 0xFFFFFFFF,
            (H[1] + b) & 0xFFFFFFFF,
            (H[2] + c) & 0xFFFFFFFF,
            (H[3] + d) & 0xFFFFFFFF,
            (H[4] + e) & 0xFFFFFFFF,
            (H[5] + f) & 0xFFFFFFFF,
            (H[6] + g) & 0xFFFFFFFF,
            (H[7] + h) & 0xFFFFFFFF,
        ]

    # produce the final hash value (big-endian) as hex
    return ''.join(f'{x:08x}' for x in H)

print("SHA-256('')  =", sha256(b""))  # expected: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
print("SHA-256('abc') =", sha256(b"abc"))  # expected: ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad