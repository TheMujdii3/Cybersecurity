# _Unknown-traffic-1_

Category | Value
-- | --
Forensics | 100

***

I inspected the original capture and noticed several **ICMP** packets carrying base64-like payloads. I extracted those packets into a separate file (`packets.pcap`), ran `strings` on it, and collected the base64 blobs. One example contained some non-printable garbage at the end, so I trimmed the extraneous bytes, base64-decoded the clean string, and recovered the flag.

### Proof-flag 
```
ctf{72c8c1090e0bba717671f79de6e941a281e2f51da29865722f98c9fa3b7160e5}```
