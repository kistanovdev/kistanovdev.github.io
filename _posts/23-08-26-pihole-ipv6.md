---
layout: til
title: "Pihole, Unbound and IPv6"
category: til
summary: "How to make Pihole work with IPV6"
---

I run a [pihole](https://pi-hole.net/) instance on my local Wi-Fi to block ads on the DNS level.
It's been running very smooth, but when I was tinkering with my local setup, I noticed
that IPv6 wasn't enabled. So, I enabled it. It's not the first time I completely nuked my Wi-Fi 
and had to figure out what is going on.

This time, instead of resetting the router to default settings, I decided to do some debugging.

```bash
ssh pihole.local
```

I am running [unbound](https://unbound.docs.nlnetlabs.nl/en/latest/use-cases/home-resolver.html),
custom DNS resolver that doesn't rely on Cloudflare (1.1.1.1) or Google (0.0.0.0).

First step in debugging is to figure out if DNS queries go out at all.
Here, we're running a DNS query but telling `dig` to use IPv6 and specify the DNS resolver with the @ sign.
```
dig AAAA ipv6.google.com @127.0.0.1
```


This resulted in a failure. 

What I learned is that unbound needs a config change to allow for IPv6.

```
sudo vim /etc/unbound/unbound.conf.d/pi-hole.conf
```

The config should have these fields set.

```
interface: ::1
do-ip6: yes
```
Now
```
sudo service unbound start
```

and voilá.
```

; <<>> DiG 9.16.42-Debian <<>> AAAA ipv6.google.com @127.0.0.1
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 41345
;; flags: qr rd ra; QUERY: 1, ANSWER: 5, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1232
;; QUESTION SECTION:
;ipv6.google.com.		IN	AAAA

;; ANSWER SECTION:
ipv6.google.com.	177	IN	CNAME	ipv6.l.google.com.
ipv6.l.google.com.	263	IN	AAAA	2607:f8b0:4002:c03::66
ipv6.l.google.com.	263	IN	AAAA	2607:f8b0:4002:c03::71
ipv6.l.google.com.	263	IN	AAAA	2607:f8b0:4002:c03::65
ipv6.l.google.com.	263	IN	AAAA	2607:f8b0:4002:c03::8a

;; Query time: 0 msec
;; SERVER: 127.0.0.1#53(127.0.0.1)
;; WHEN: Sat Aug 26 11:01:47 PDT 2023
;; MSG SIZE  rcvd: 187
```
