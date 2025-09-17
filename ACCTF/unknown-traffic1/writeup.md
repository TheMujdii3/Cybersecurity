I opened the original file and took a look around and managed to observe that some icmp packets had some base64 data. So i got them in a separate file (separate packets.pcap) and used 'strings "separate packets.pcap"' and got those b64 encoded strings (Y3RmezcyYzhjMTA5MGUwYmJh␏ºæ␄NzE3NjcxZjc5ZGU2ZTk0MWEyODFlMmY1MWRhMjk4NjU3MjJmOThjOWZhM2I3MTYwZTV9) and got the flag.

# ctf{72c8c1090e0bba717671f79de6e941a281e2f51da29865722f98c9fa3b7160e5}
