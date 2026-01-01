---
date: '2025-12-17T14:23:46+08:00'
draft: true
title: 'Example Page'

math: true

# weight: 1
# aliases: ["/first"]
tags: ['first']
author: 'Me'
# author: ["Me", "You"] # multiple authors
showToc: true
TocOpen: false
hidemeta: false
comments: false
description: 'Desc Text.'
canonicalURL: 'https://canonical.url/to/page'
disableHLJS: false # to disable highlightjs
disableShare: false
hideSummary: false
searchHidden: true
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true
ShowWordCount: true
ShowRssButtonInSectionTermList: true
UseHugoToc: true
cover:
  # image: '<image path/url>' # image path/url
  image: 'https://i.ibb.co/K0HVPBd/paper-mod-profilemode.png'
  alt: '<alt text>' # alt text
  caption: '<text>' # display caption under cover
  relative: false # when using page bundles set this to true
  hidden: false # only hide on current single page

editPost:
  URL: 'https://github.com/<path_to_repo>/content'
  Text: 'Suggest Changes' # edit text
  appendFilePath: true # to append file path to Edit link
---

## Introduction

Raw Mathjax block:

$$a_4 \ne b_4$$

Let $n$ be a natural number, and define $m := n^2 + 1$. Then ...

This shows as Mathjax \\(a \ne b\\), but this doesn't \(a \ne b\)

$$ 10^4 $$

This is **bold** text, and this is _emphasized_ text.

Visit the [Hugo](https://gohugo.io) website!

This is a post about latex.

An equation:
$$\int_{-\infty}^{\infty} e^{-x^2} dx$$. <!-- works -->

inline example: $\sum_{i = 0}^N 2i = y$ <!-- works -->

One overbrace:

$${a}^{b} - \overbrace{c}^{d}$$ <!-- works-->

Two overbraces:
$$\underbrace{a}_{b} - \underbrace{c}_{d}$$ <!--does not work -->

None of these below works properly:

$$
\begin{aligned}
        equation &= 16 \\
        other &= 26 + 13
\end{aligned}
$$

$$
\begin{pmatrix}
   a & b \\
      c & d
      \end{pmatrix}
$$

This is a post about latex.

An equation:
$$\int_{-\infty}^{\infty} e^{-x^2} dx$$. <!-- works -->

inline example: $\sum_{i = 0}^N 2i = y$ <!-- works -->

One overbrace:

$${a}^{b} - \overbrace{c}^{d}$$ <!-- works-->

Two overbraces:
$$\underbrace{a}\_{b} - \underbrace{c}_{d}$$ <!--does not work -->

None of these below works properly:

```katex
$$
\begin{aligned}
        equation &= 16 \\\
        other &= 26 + 13
\end{aligned}
$$
```

Let $n$ be a natural number, and define $m := n^2 + 1$. Then ...
