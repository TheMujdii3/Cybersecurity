# _Unknown-traffic-2_

Category | Value
-- | --
Forensics | 100

***

I inspected the capture and noticed several HTTP packets carrying chunked payloads. Using Wireshark I filtered for those packets with:

```
(frame contains "chunk") && (_ws.col.protocol == "HTTP")
```

I exported the matching packets as `chunks.pcap`, extracted and reassembled the chunked bodies, and reconstructed the embedded image (`imagine.png`). Scanning the QR code in that image revealed the flag.
