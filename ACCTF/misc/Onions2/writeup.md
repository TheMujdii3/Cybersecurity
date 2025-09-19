# _onions2_

Category | Value
-- | --
Misc | 162

***

First, when I saw the image I immediately loaded it into Aperisolve to see what I could get with minimal effort.
While exploring the results I found an `.onion` link and accessed it. In the page source I noticed a custom font, so I downloaded and analyzed it briefly. Using `strings` I found sequences like `"MmQgMmQgMm"`, which translate to hex values (`2d 2d 2d 2d 2d 20 2e 2d 2…`) corresponding to `-` and `.` — in other words, Morse code.

Decoding the Morse produced a Google Maps URL:

```
https://www.google.com/maps/place/ARChA/@45.7450165,21.225122,17z/data=!4m16!1m9!3m8!1s0x47455d9b87725af1:0x7a82191592d97493!2sARChA!8m2!3d45.7450165!4d21.2277023!9m1!1b1!16s%2Fg%2F11vbtv2ys4!3m5!1s0x47455d9b87725af1:0x7a82191592d97493!8m2!3d45.7450165!4d21.2277023!16s%2Fg%2F11vbtv2ys4?entry=ttu&g_ep=EgoyMDI1MDkxMC4wIKXMDSoASAFQAw%3D%3D
```

That Maps entry contains a photo with a QR code — the QR code held the flag.
