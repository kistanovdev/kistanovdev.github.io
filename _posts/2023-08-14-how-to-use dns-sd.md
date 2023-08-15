---
layout: til
title: "How to use dns-sd"
category: til
summary: "dns-sd is a handy utility"
---

Today I was troubleshooting why some of my smart home devices weren't showing up on my Wi-Fi network.
Turns out, not all of them are going to show up correctly. In order to find them, you may need to run some mDNS queries with  `dns-sd` installed by default on macOS.

First, you can query what types of protocols are available to you.

```
dns-sd -B _services._dns-sd._udp | awk '{ print $NF }'
```

After some filtering/cleanup, my list looked like this. 
```
_sleep-proxy
_raop
_companion-link
_meshcop
_srpl-tls
_matter
_ltpdu
_hap
_spotify-connect
_sleep-proxy
_matter
_meshcop
_ltpdu
_hap
_srpl-tls
_rdlink
_aqara-setup
_hap
_pdl-datastream
_printer
_ipp
_scanner
_http
_uscan
_raop
_companion-link
_airplay
```
You may query each one of them with the following command 
```
dns-sd -B _ltpdu._udp.
```
and may get something like this in response

```
Instance Name
Nanoleaf A19 DE0-EB91
Nanoleaf A19 1WWJ
Nanoleaf A19 96M2
Nanoleaf A19 4565
Nanoleaf A19 3R4X
```

Let's query one of them 
```
dns-sd -L "Nanoleaf A19 DE0-EB91" _ltpdu._udp.
```
and we get 

```
Nanoleaf\032A19\032DE0-EB91._ltpdu._udp.local. can be reached at B6A77EC42FDCBA97.local.:5653 (interface 15)
 xp=609841E38E704518 srcvers=3.2.0 md=NL67 eui64=B43A31FFFED909F7 id=EB91
 ```

Now let's do another query 
```
dns-sd -G v4 B6A77EC42FDCBA97.local.:5653
```

We get the follwoing. I removed IP address for security reasons.

```
Hostname                      Address         TTL
B6A77EC42FDCBA97.local.:5653. <REDACTED>      77
```

It seems to point to some DigitalOcean server in New York.
I guess that's an investigation for another day.
