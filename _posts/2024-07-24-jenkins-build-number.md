---
layout: post
title: "Jenkins Build Number"
category: til
summary: "TIL that jenkins returns the build number in the damn header"
draft: false
---

When you send stuff to a jenkins instance with `buildWithParams?`, I used to think
that the response comes back empty. I thought to myself, "Oh, that's bad design.".
TIL, Jenkins actually returns the stuff in the damn header...
