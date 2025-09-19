```markdown
# _disco_dance_

Category | Value
-- | --
Misc | 218
```

The handout was quite self-explanatory: grab the **last five messages** from the specified Discord channel, concatenate them as a **key seed**, and use that to decrypt the provided ciphertext with **AES-CBC**. The first **16 bytes** of the blob are the **IV**; the remainder is the encrypted flag.

### Solver

```python
import base64, hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

encrypted_b64 = "Uo5S4xvMZOQn8SVpx25eLmSlvVdYb4Wuw3ofh/zMbi/Kqeh6KaCvsS7R7Me7OXNJtXJFRnlUBKgzBTgPg+QgrO29hBDYUw5qlmGlrBuq15IF9Nd80o7Ctvdw4HtzRffK"

# last five Discord messages (order preserved)
msgs = ["b","b","b","b","b"]

seed = "".join(msgs).encode()
key  = hashlib.sha256(seed).digest()

raw = base64.b64decode(encrypted_b64)
iv, ct = raw[:16], raw[16:]

pt = unpad(AES.new(key, AES.MODE_CBC, iv).decrypt(ct), AES.block_size)
print(pt.decode("utf-8", errors="ignore"))
```

### Proof of flag

```
CTF{f55ba4939edd5611a7ab797529b51dae47989b3c5a99f2ffc82e4b2c74d03e56}
```