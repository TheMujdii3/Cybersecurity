I took a look around and and observed that some http packets have chunks of data in them. I used this filter in wireshark "(frame contains "chunk") && (_ws.col.protocol == "HTTP")" and managed to get all http packets with chunks of data (chunks.pcap).
After that i used chatgpt for faster processing and got an image containing a qr code (imagine.png) which contains the flag.
