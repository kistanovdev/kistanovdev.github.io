---
layout: til
title: "Patchfiles and git"
category: til
summary: "How to take advantage of patchfiles and git"
draft: false
---


In git, I prefer the following workflow:

- keep history as linear as possible because nobody cares or wants to see your "fix typo" git comment
- always rebase on top of existing changes and squash if you cannot 


However, I had a fortune of working on a very large project of upgrading java infrastucture. One
of the base libraries had thousands of changes after everything was set and done and rebasing the changes to clean up the git history was time consuming and required all people who worked together to advise on how to resolve merge conflicts. The solution to this tiresome problem is using a patchfile.


From [this stack overflow answer](https://stackoverflow.com/questions/16675766/get-the-difference-between-two-branches-in-git),
```
git diff master Branch1 > ../patchfile
git checkout Branch2    
git apply ../patchfile
```

This saved me about an hour of working through the interactive rebase.
