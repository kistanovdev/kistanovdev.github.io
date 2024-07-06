---
layout: post
title: "Django Tutorial: Url Shortner (pt. 2)"
category: blog
summary: "A beginner's guide to writing a useful Django App Part 1"
draft: true
---


# Writing our application

Let's sketch out the design of our app.

1. A user will go to the landing page and be presented with an option
   to paste a link and get a short version of their url. A user cannot paste an invalid link.
2. Upon success, the user will be presented with a short version of their url.
3. If the user decides to go through the url, the server will forward the user to a correct place.

So, our plan will be
1. Add our html pages
2. Design the schema for the url lookup table
3. Design the landing page view, success view and redirect views

### templates folder

So far we have 5 files in our Django server. Let's add two more.
Create a folder called `templates` under the `app` and add two files:
`landing_page.html` and `success.html`. Let's go ahead and paste the minimum
required to render an html document into both files.
```
<!DOCTYPE html>
<html>
<body>
</body>
</html>
```

### managing views

Now we arrive at a very important concept in Django, the `views`. Django follows a
[MVC Design Pattern](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller).
Let's add our first django view called landing page. I will add some basic types

```python3
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
def landing_page_view(request: HttpRequest) -> HttpResponse:
    return render(request, template_name="landing_page.html")
```
Please note 3 new concepts.
1. `render` function from `django.shortcuts` provides a convenient way
   of rendering an html file.
2. Our function takes a request object of type `HttpRequest`. It contains all information
   related to the http request.



