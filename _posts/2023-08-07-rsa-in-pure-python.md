---
layout: post
title: "Generating RSA keys in pure python"
category: blog
summary: "Inspired by Andrei Karpathy's blog about generating RSA keys in python"
draft: true
---

At the end of the article, we will be able to run our python code and generate private
RSA keys similar to this `openssl genrsa` command 
```
Generating RSA private key, 2048 bit long modulus
e is 65537 (0x10001)
-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAzhfxZxL2svDJ0wbXrlf/MWZrOEv8R5W1I3LieyDP6fIq3Ni8
[REDACTED]
-----END RSA PRIVATE KEY-----
```

If you don't know anything about RSA and public key cryptography,
I would recommend starting with [this wikipedia article](https://en.wikipedia.org/wiki/RSA_(cryptosystem))
and this [youtube video](https://www.youtube.com/watch?v=4zahvcJ9glg) by the amazing Eddie Woo.


## Operating on large numbers
By design, most modern programming languages can handle integers up to 2^128 natively.
For anything larger than that, we would use specialised libraries
like [GMP](https://gmplib.org/). We're in luck though, because python natively supports arbitrary large numbers. 
They're not fast, but when it comes to programming in python, you're not looking for speed anyway.


## Algorithm

1. Generate 2 primes `p` and `q`, each 1024 bit length.
2. Compute `n=pq`
3. Compute `λ(n)`, where `λ` is a [Carmichael function](https://en.wikipedia.org/wiki/Carmichael%27s_totient_function). 
4. choose number `e`. For our case, e will be 65537, which is the most commonly chosen value.
5. Determine `d`, where `de ≡ 1 (mod λ(n))`.

## Functions we'll need

First, here's a function to read 1024 bits from `/dev/random`.

```
def generate_random_number():
    with open('/dev/random', 'rb') as f:
        rand_bytes = f.read(128)
        rand_int = int.from_bytes(rand_bytes, 'big')
        return rand_int
```
GCD
```
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
```
Least common denominator or lcm
```
def lcm(p, q):
    p -= 1
    q -= 1
    return (p * q) // gcd(p, q)
```
Inverse mod
```
def mod_inv(e, mod):
    if gcd(e, mod) != 1:
        return None
    else:
        u1, u2, u3 = 1, 0, e
        v1, v2, v3 = 0, 1, mod
        while v3 != 0:
            q = u3 // v3
            v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
        return u1 % mod
```
sieve check to speed up the process
```


def quick_sieve_check(candidate):
    """
    first_hundred_primes = {***}
    for prime in first_hundred_primes:
        if candidate % prime == 0:
            return True

    return False
```
Finally, the Miller-Rabin primality test that can be found on page 72 of this [doc](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.186-4.pdf)
```
def miller_rabin_primality_test(candidate):
    if candidate % 2 == 0:
        return False

    if quick_sieve_check(candidate):
        return False
    
    minus_one = candidate - 1
    m = copy(minus_one)
    a = 0
    while m % 2 == 0:
        m >>= 1
        a += 1

    miller_rabin_iterations = 4
    for _ in range(miller_rabin_iterations):

        base = random_in_range(2, candidate - 1)
        
        z = pow(base, minus_one, candidate)
        if z in (1, minus_one):
            continue

        for _ in range(1, a):
            z = pow(z, 2, candidate)
            if z == minus_one:
                break
            if z == 1:
                return False
        else:
            return False

    return True
```
