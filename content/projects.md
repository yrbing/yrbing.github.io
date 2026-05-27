---
title: 'Projects'
layout: 'page'
---

A few things I've shipped recently. Independent builds where I owned the full stack, from design to deployment.

{{< project-card id="chess" >}}

> **Why I built it:** I picked up chess last year on Duolingo. Playing against their AI Oscar, I only ever learned the outcome (win, lose, or draw), never _why_ a move was good or bad. The analysis sites I tried buried beginners in jargon. So I built my own chess app: an opponent I can practice against, with hints that actually explain the right move. The goal is simple: for every beginner to understand their moves.

- ♟️ **AI Opponent:** Integrated Stockfish (WASM) in a Web Worker, exposing three difficulty tiers (~400 / ~1500 / ~2800 Elo) via `UCI_LimitStrength` and configurable search depth.
- 🧠 **Game Engine:** Wrapped `chess.js` in a custom `useChessGame` hook to manage move validation, SAN history, undo, and end-state detection (check / checkmate / draw).
- 💡 **Player UX:** Built hint suggestions, captured-piece tracking, two-player pass-and-play mode, and a scrubbable move history for post-game review.
- 🎨 **Theming:** Designed light/dark UI modes plus six board color schemes, persisted in `localStorage` and applied via `data-theme` and CSS variables.
  {{< /project-card >}}

{{< project-card id="blog" >}}

- 🎨 **Brand & UX:** Tailored theme aesthetics and interaction logic with custom CSS/JS for a personalized brand experience.
- 🚀 **CI/CD:** Streamlined deployment via GitHub Actions, ensuring high availability and seamless content updates.
- 🧩 **Custom Shortcodes:** Built a D3-powered word-cloud shortcode and a Swiper carousel shortcode reused across posts.
  {{< /project-card >}}
