"""
A small cli to make either a TIL post or Regular Post
"""

import sys
from string import Template
from datetime import datetime
import os

ALLOWED_TYPES = ["til", "blog", "bookmark"]

with open("templates/post.template", "r") as template:
    t = Template(template.read())

post_type = input(f"Is this a TIL or Regular Post? [{'/'.join(ALLOWED_TYPES)}] ")

if post_type not in ALLOWED_TYPES:
    print("Please enter either 'til' or 'post'")
    sys.exit(0)

title = input("What is the title? ").lower()
summary = input("What is the summary? ")

today = datetime.now().strftime("%Y-%m-%d")
file_title = today + "-" + "-".join(title.split(" ")) + ".md"

file_path = os.path.join("_posts", file_title)
with open(file_path, "w") as f:
    f.write(t.substitute(type=post_type, title=title, summary=summary, category=post_type))
