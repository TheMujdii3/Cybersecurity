First I searched for other challs related to arcade games and found absolutely nothing:)
Then I thought hmm maybe the author left me some clues embedded in the .nes file and used strings again which was a good move to be honest
I found multiple strings like this one "30$$$36$$$38$$$30$$$62$$$66$$$36$$$31$$$36$$$30$$$32$$$31".If you exclude the $$$ it looks like hex data and this is exactly what i did.
I took every each one of those strings and put them in cyberchef used replace to get rid of the $$$ and from hex to get the final flag.
