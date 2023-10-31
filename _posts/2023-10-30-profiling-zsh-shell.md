---
layout: til
title: "Profiling Zsh shell"
category: til
summary: "How to profile slow startup shell"
---

You can put `zmodload zsh/zprof` at the top of your 
zsh file and `zprof` at the bottom to profile the performance
of your shell startup.

I was able to speed up my shell startup by a lot.
