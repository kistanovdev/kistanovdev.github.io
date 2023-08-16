---
layout: til
title: "Fancy css transition on hover"
category: til
summary: "How to do CSS transitions on hover"
---

I hate CSS, but sometimes you just can't avoid it.
Today I learned about how to make nice transitions with CSS using `hover` tag.

First, let imagine we have the following CSS for our image 

```css
.about_logo {
    float: left;
    width: 187px;
    height: 193px;
    margin-left: -220px;
    margin-top: -13px;
    background: url("/i/logo.png");
    background-size: 200px;
}
```
In order to make it transition to another image we need to add the following

```css
/* continued */
   background-size: 200px;
   transition: background-image 0.5s ease-in-out;
}
.about_logo:hover {
    background-image: url("/i/logo_color.png");
}
```
You should be able to see the logo on the footer. Hover over it, see what happens.


You may read more about hover tag [here](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/hover).
