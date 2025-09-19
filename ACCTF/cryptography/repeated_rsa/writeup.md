# _Repeated RSA_

Category | Value
-- | --
Crypto | 100

***

For this challenge I once again turned to my friend GPT. I provided the outputs from two separate connections to the service, and with that it helped me piece together the attack and recover the flag.

The vulnerability was that the same plaintext was repeatedly encrypted under three related RSA moduli. With some GCD tricks, the factors overlap and you can reconstruct the private keys.

### Proof of concept script

```python
from math import gcd

def inv(a, m):  # Python 3.8+: pow(a, -1, m) works too
    return pow(a, -1, m)

def fact_triple(n1, n2, n3):
    p12 = gcd(n1, n2); p13 = gcd(n1, n3); p23 = gcd(n2, n3)
    assert n1 == p12 * p13 and n2 == p12 * p23 and n3 == p13 * p23
    return ((n1, (p12, p13)), (n2, (p12, p23)), (n3, (p13, p23)))

def solve(c, n1, n2, n3, e=65537):
    facts = fact_triple(n1, n2, n3)
    keys = []
    for n, (p, q) in facts:
        phi = (p - 1) * (q - 1)
        d = inv(e, phi)
        keys.append((n, d))
    # Encryption order was n1 -> n2 -> n3, so decrypt in reverse
    x = pow(c, keys[2][1], keys[2][0])
    x = pow(x, keys[1][1], keys[1][0])
    m = pow(x, keys[0][1], keys[0][0])
    return m.to_bytes((m.bit_length() + 7) // 8, 'big')

# Fill in c, n1, n2, n3, then print(result.decode())
```

ChatGPT chat: [https://chatgpt.com/share/68c70579-f9d8-8006-80e3-508155aa5583](https://chatgpt.com/share/68c70579-f9d8-8006-80e3-508155aa5583)

## Proof-of-flag
```
ctf{3c1315f63d550570a690f693554647b7763c3acbc806ae846ce8d25b5f364d10}
```