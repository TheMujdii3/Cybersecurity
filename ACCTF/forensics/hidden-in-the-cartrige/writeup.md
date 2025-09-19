# _Hidden-in-the-cartridge_

Category | Value
-- | --
Forensics | 100

***

I looked for other arcade-related challenges first and found nothing. Then I inspected the `.nes` ROM with `strings` and noticed repeated patterns like:

```
30$$$36$$$38$$$30$$$62$$$66$$$36$$$31$$$36$$$30$$$32$$$31
```

Removing the `$$$` produced a hex string (`303638306266363136303231`), which I decoded as hex. I automated this in CyberChef by replacing `$$$` with nothing and running **From Hex** to reveal the flag.

### Proof-of-flag 
```
ctf{9f1b438164dbc8a6249ba5c66fc0d6195b5388beed890680bf616021f2582248}
```
