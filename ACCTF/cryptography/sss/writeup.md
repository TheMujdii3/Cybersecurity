I used chatgpt to generate a decoding script for this chall. 
# The script: 
`
import re

IRR = 0x11B  # x^8 + x^4 + x^3 + x + 1

def only_hex(s: str) -> str:
    return ''.join(ch for ch in s if ch.lower() in '0123456789abcdef')

def h2b_strict(tag: str, h: str) -> bytes:
    h = only_hex(h)
    if len(h) % 2 == 1:
        print(f"[!] Warning: odd hex length in {tag} ({len(h)}). Dropping last nibble.")
        h = h[:-1]
    return bytes(int(h[i:i+2], 16) for i in range(0, len(h), 2))

def gf_mul(a: int, b: int) -> int:
    res = 0
    for _ in range(8):
        if b & 1:
            res ^= a
        hi = a & 0x80
        a = (a << 1) & 0xFF
        if hi:
            a ^= IRR & 0xFF  # 0x1B after dropping x^8
        b >>= 1
    return res

def gf_pow(a: int, e: int) -> int:
    r = 1
    while e:
        if e & 1:
            r = gf_mul(r, a)
        a = gf_mul(a, a)
        e >>= 1
    return r

def gf_inv(a: int) -> int:
    if a == 0:
        raise ZeroDivisionError("gf_inv(0)")
    # In GF(256), a^255 = 1 for a != 0  -> a^-1 = a^254
    return gf_pow(a, 254)

def parse_share(raw: bytes):
    if len(raw) < 3:
        raise ValueError("Share too short")
    if raw[0] == 0x80:
        x = raw[1]
        y = raw[2:]
    else:
        x = raw[0]
        y = raw[1:]
    if x == 0:
        raise ValueError("Invalid share: x = 0")
    return x, y

def lagrange_lambdas_at_zero(xs):
    # λ_i(0) = Π_{j≠i} (x_j / (x_i - x_j)) over GF(256)
    ls = []
    for i, xi in enumerate(xs):
        num = 1
        den = 1
        for j, xj in enumerate(xs):
            if j == i:
                continue
            num = gf_mul(num, xj)
            den = gf_mul(den, xi ^ xj)  # subtraction == XOR in GF(2^8)
        li0 = gf_mul(num, gf_inv(den))
        ls.append(li0)
    return ls

def reconstruct(P1_hex: str, P2_hex: str, P3_hex: str):
    P1_raw = h2b_strict("P1", P1_hex)
    P2_raw = h2b_strict("P2", P2_hex)
    P3_raw = h2b_strict("P3", P3_hex)

    x1, y1 = parse_share(P1_raw)
    x2, y2 = parse_share(P2_raw)
    x3, y3 = parse_share(P3_raw)

    L = min(len(y1), len(y2), len(y3))
    y1, y2, y3 = y1[:L], y2[:L], y3[:L]

    l1, l2, l3 = lagrange_lambdas_at_zero([x1, x2, x3])

    secret = bytearray(L)
    for i in range(L):
        acc = 0
        acc ^= gf_mul(y1[i], l1)
        acc ^= gf_mul(y2[i], l2)
        acc ^= gf_mul(y3[i], l3)
        secret[i] = acc
    return bytes(secret)

def to_hex(b: bytes) -> str:
    return ''.join(f"{x:02x}" for x in b)

def best_ascii(b: bytes) -> str:
    return ''.join(chr(x) if 32 <= x <= 126 else '.' for x in b)

if __name__ == "__main__":
    P1 = "8010ba0d6ed38ef563074c3ee80a44f7fe680e82015a8d35f7f2245f66ec9c889b4e31a0c3e97bceeb6f28695f7a494918e0ca079677f07fff8eb570c17a4cb1db0477b84e9c68b9f02b21b33850f33bbd18f886b65c1f3bb015ddbe2723e64abfe8595e181d69d3f8ca3b7cc01c875ea25b97ef1e171c4f3f887e5752541270ae461cc610b3eb422c34df84e7b9a567f7933ee4b6969d19273d212a3ee92f8509679a4b40b6823c007e6d5c6241959e86bc8f989754649cd3008bdbb5bf030c9e802adf54d3afce4edef9bb709c7db4c2ac1f96f3e05cd220534b5647f35888e0e3d2435abdb1d7f32413bb630b3e8b0502e774dda8ac2bd4c2623ac433f79bd12"
    P2 = "80264e325aa037314746964303cf6fee98d64e1e03d613fb8f327f5241850adbd06e1f959bdb6e5bd35874188e3fa4740a1948befcacb8949350574825ba4519793a6a617048fb2f5bdd9bc3267a61051484ec16e83ff7baaafac81a3aa4fb2077da312ee4f00c705b8f626334ff3045e41f451858988a3549e314f8a70f0879f5a30fbcd5fcc1645575186af8a434876304bb1ebc360533389143f7d918682307736bac713b63338482ef1cf80ac415f213625231ef3d3bdd70f811c8cc7515cf83a74ea25c31264a9a5dbe0615c5959e181bf8effa1698ece11cb5e9c794d381311ba1900f0c550f33b61fd49959d9b4ba73588b14906fddb625bd13f7149a95a"
    P3 = "8036f43f3473b9c42441da7debc52b1966be409c028c9ece78c05b0d276996534b202e355832159538375c71d145ed3d12f982b96adb48eb6cdee238e4c009a8a23e1dd93ed49396abf6ba701e2a923ea99c14905e63e8811aef15a41d871d6ac8326870fced65a3a345591ff4e3b71b4644d2f7468f966a71bb698ff6cb198958d5105ac65f2c367a31c4fe1c0d97b09717867a09209e0a1cac64ede1c144d60854f7c7321de22f82ec8470991b57db729feb8aa0eb5ab7081070aa7b33755952238b81f5cf9dc80724a26575d9bba15ae4027e1f9a490acfd25183adb4ca1b62a2ca92c9a2bee2fa27a634b4b26402b298975c509c3f240f344037d1a4e44142b"

    secret = reconstruct(P1, P2, P3)
    print("[+] Secret bytes (hex):", to_hex(secret))
    ascii_view = best_ascii(secret)
    print("[+] ASCII preview     :", ascii_view)

    m = re.search(r'(?i)ctf\{[^}]+\}', ascii_view)
    if m:
        print("[+] Flag              :", m.group(0))
    else:
        print("[i] No ctf{...} found in ASCII preview. If the flag is encoded,")
        print("    try decoding the hex/bytes above (e.g., base64, zlib, etc.).")
`
and got the flag.

# Flag: ctf{d6b72529c6177d8f648ae85f624a24d6f1edce5ca29bd7cc0b888e117a123892}
