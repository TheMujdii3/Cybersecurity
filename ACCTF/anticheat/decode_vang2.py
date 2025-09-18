#!/usr/bin/env python3
import struct
import sys
import os

def rc4(data, key):
    S = list(range(256))
    j = 0
    out = []

    # Key Scheduling Algorithm (KSA)
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]

    # Pseudo-Random Generation Algorithm (PRGA)
    i = j = 0
    for char in data:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        out.append(char ^ S[(S[i] + S[j]) % 256])

    return bytearray(out)

KEYMASK = [
    0xB1, 0x54, 0x45, 0x57, 0xA7, 0xC4, 0x64, 0x2E,
    0x98, 0xD8, 0xB1, 0x1A, 0x0B, 0xAA, 0xD8, 0x8E,
    0x7F, 0x1E, 0x5B, 0x8D, 0x08, 0x67, 0x96, 0xCB,
    0xAA, 0x11, 0x50, 0x84, 0x17, 0x46, 0xA3, 0x30
]

def main():
    if len(sys.argv) <= 1:
        print(f"Usage: {sys.argv[0]} <vgc_X_Y_Z.log>")
        sys.exit(1)

    filepath = sys.argv[1]

    if not os.path.isfile(filepath):
        print(f"File not found: {filepath}")
        sys.exit(1)

    with open(filepath, "rb") as f:
        DATA = f.read()

    if len(DATA) < 4 + 32:
        print("Invalid file: too short")
        sys.exit(1)

    DATA = DATA[4:]  # skip magic?
    REAL_KEY = [DATA[i] ^ KEYMASK[i] for i in range(32)]
    DATA = DATA[32:]

    index = 0
    while len(DATA) > 0:
        if len(DATA) < 4:
            print("Malformed block header")
            break

        BLOCK_LEN = struct.unpack("<L", DATA[:4])[0]
        DATA = DATA[4:]

        if len(DATA) < BLOCK_LEN:
            print(f"Incomplete block at index {index}")
            break

        try:
            decrypted = rc4(DATA[:BLOCK_LEN], REAL_KEY).decode("utf-16")
            print(f"[{index}] ✅ {decrypted}")
        except Exception as e:
            print(f"[{index}] ❌ Failed to decode block: {e}")

        DATA = DATA[BLOCK_LEN:]
        index += 1

if __name__ == "__main__":
    main()

