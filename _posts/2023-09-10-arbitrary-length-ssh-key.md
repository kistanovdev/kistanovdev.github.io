---
layout: til
title: "Arbitrary legth RSA keys"
category: til
summary: "How to generate large ssh keys"
---

The usual size of an RSA key varies between 1024 and 4096 bits.
Keys larger than 4096 are considered impractical when comparing
time to generate and use one vs security tradeoff.
Even though it is impractical, nobody said it's impossible.
You may generate RSA keys larger than the 4096-bit max convention size.
The problem, of course, is that you may spend an eternity 
trying to generate it.

For example, we may use the following command to generate 32768-bit 
RSA key
```
openssl genpkey -algorithm RSA -out privatekey.pem -pkeyopt rsa_keygen_bits:32768
```
It took my M2 Max around 40 min to complete the useless task.
```
2408.53s user 3.39s system 99% cpu 40:15.02 total
```

