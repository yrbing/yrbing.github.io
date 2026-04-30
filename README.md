# Robin's Blog

A personal blog and portfolio site by Robin Yang, built with [Hugo](https://gohugo.io/) and the [PaperMod](https://github.com/adityatelange/hugo-PaperMod) theme.

## Getting started

Prerequisites: [Hugo](https://gohugo.io/installation/) (extended) and Git.

```sh
git clone --recurse-submodules https://github.com/yrbing/yrbing.github.io.git
cd robin-blog
hugo server -D
```

The site will be available at http://localhost:1313. The `-D` flag includes draft posts.

## Writing

Create a new post:

```sh
hugo new posts/my-new-post.md
```

Posts live in `content/posts/`. Front matter follows the PaperMod conventions — see existing posts for examples.

## Tag word cloud

The "About" page renders a word cloud from post tags. After adding or editing tags, regenerate the data file:

```sh
python scripts/generate_tags.py
```

This writes `data/wordcloud.json`, which the homepage reads at build time.

## Project layout

```
content/      Markdown posts and pages
layouts/      Theme overrides and custom shortcodes
assets/       SCSS, JS, and images processed by Hugo Pipes
static/       Files copied verbatim to the site root
data/         Build-time data (e.g. wordcloud.json)
scripts/      Helper scripts
themes/       PaperMod theme (git submodule)
hugo.yaml     Site configuration
```

## Building for production

```sh
hugo --minify
```

The static site is generated into `public/`.
