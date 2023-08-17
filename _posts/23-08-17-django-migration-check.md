---
layout: til
title: "Django Migrations Check"
category: til
summary: "A nice way to verify that your migraions are good"
---

Recently I learned a quick way to check if you migrations are up to date.

At work, I used wrote something like this:

```
#!/bin/bash

pip install -r req/dev.txt

python manage.py makemigrations

git add .

if ! git diff-index --quiet HEAD --; then"
    exit 1
else
    exit 0
fi
```

It can be simplifies with the following command 

```
python manage.py makemigrations --check --dry-run
```
