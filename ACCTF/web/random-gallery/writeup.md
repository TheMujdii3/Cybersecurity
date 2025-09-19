# _random_gallery_

Category | Value
-- | --
Web | 100

***

At first I assumed I needed to set the `isLogged` cookie to `true`, but that wasn’t it. What did help was curling the login endpoint with the provided cookies:

```bash
curl -s -v http://ctf.ac.upt.ro:9465/login \
  -H "Cookie: logged_in=True; session=978fa8b1-8dff-4239-8395-5733c8ed44c2.y97WYSrEJ78X6o6v0Xt2HCM-M"
```

The response revealed a `/gallery` endpoint. I visited it in the browser without bothering to change the cookie values and found several photos, one of which contained a QR code. Scanning that QR gave a ***pastebin* link.
```
https://pastebin.com/9HibccWH
```

## Proof-of-flag
```
ctf{1cd4daf060aee882653595cca4e719d48a3080cd1b76055812145da8a10b47e1}
```
