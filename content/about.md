---
title: 'About Me & Resume'
layout: 'page'
---

{{< wordcloud dataSource="skills" >}}

**Hi, I'm Robin 👋**

I'm a **Senior Full-Stack Engineer** with 7+ years of experience. What I love most about this craft is using technology to bring a little more joy, ease, warmth, and delight into people's lives.

**🎨 Beyond the Editor**

When I'm not in a codebase, you'll find me:

- 🎥 **Filming & Editing:** Short films on my Osmo Pocket 3, shared on Xiaohongshu (RED).
- 📚 **Reading & Writing:** Books, essays, and the deep-dive posts on this blog.
- 🩰 **Ballet & Weightlifting:** Daily training for focus and strength.
- ♟️ **Chess:** Practising on Duolingo Chess, challenging Oscar every day.

**📂 Featured Projects**

A couple of projects I've built end-to-end, just for fun.

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

---

> **Curious about the day job?**
> You can find my full resume below. If you're interested in my work experience or would like to discuss potential collaborations, feel free to [jump to the experience section](#-professional-experience) or [reach out directly](#-get-in-touch).
>
> [📥 Download PDF Version](/Robin_Yang_CV.pdf)

---

# Robin Yang

**Senior Full-Stack Engineer**  
📍 Auckland, New Zealand

## 🚀 Summary

Senior Full-Stack Engineer with **7+ years** of experience at global tech leaders including **ByteDance (TikTok)** and **Xiaomi**. **5 of those years** were spent building hybrid mobile applications across mobile web/H5, WeChat mini-apps, and React Native. Specialise in architecting full-stack web applications and cloud-native platforms across the **React and Node.js ecosystem**, from GraphQL/REST API design 🔧 to high-performance **UI/UX delivery** 🎨. Strong focus on platform-scale systems and AI-assisted development practices. Now based in **Auckland** and contributing locally through Auckland City Mission while seeking the next senior role in New Zealand's tech sector.

## 🛠 Technical Skills

- **Languages:** TypeScript, JavaScript (ES6+), HTML5, CSS3 (SCSS, Tailwind CSS, styled-components)
- **Frameworks & Libraries:** React (Hooks, Context, Router), Next.js, Redux, Zustand, TanStack Query
- **Engineering & DevOps:** Webpack, Vite, CI/CD (GitLab CI/CD, GitHub Actions), Git Flow, Docker, Kubernetes
- **Cloud & Platform Engineering:** Cloud-native architecture (public/private/hybrid, multi-cloud), PaaS platform design, Kubernetes (multi-cluster management)
- **AI-Assisted Development:** Claude Code, Claude Design
- **Testing:** Jest, Vitest, React Testing Library, Playwright
- **Performance:** Core Web Vitals, Chrome DevTools, Bundle Optimization, Code Splitting
- **Cross-Platform & Mobile:** Hybrid App, JSBridge, React Native, WebView, Mobile Responsive Design
- **Backend:** Node.js, Express/Koa, GraphQL, RESTful APIs, WebSocket
- **Databases:** MongoDB
- **Leadership & Collaboration:** Mentoring, Cross-functional Collaboration, Team Communication, Problem-Solving, Workflow Organisation, Technical Leadership, Code Review

## 💼 Professional Experience

### Auckland City Mission
_Volunteer Software Engineer_

📅 Apr 2026 – Present · [missiongrocer.co.nz](https://www.missiongrocer.co.nz/)

- **Digital Transformation:** Modernised Mission Grocer's Shopify e-commerce infrastructure using Liquid, custom JS/CSS, and Shopify CLI, applying web accessibility standards throughout, and driving end-to-end digital transformation. Established the first engineering workflow from scratch, introducing a structured Dev-Review-Release lifecycle with reliable rollback strategies to ensure zero production downtime.
- **AI-Assisted Delivery:** Introduced **Claude Design** and **Claude Code** as the organisation's standard AI-assisted development workflow, accelerating feature delivery while maintaining code quality.
- **Event Marketing:** Partnered with the Project Manager to architect full-cycle event marketing infrastructure for the Auckland Food Show. This included a pre-event landing page, on-site QR sign-up, and post-event thank-you email. The result: per-event conversion tracking and data-driven, personalised lifecycle marketing campaigns.

### TikTok
_Senior Full-Stack Engineer_

📅 Apr 2019 – Aug 2023

- **Team Leadership:** Led a team of 5 front-end engineers to deliver Douyin Consumer Finance's in-app hybrid experience, integrating iOS, Android and backend, serving **10M+ DAU**.
- **Architecture Migration:** Spearheaded the legacy migration from **Vue.js** to **React + TypeScript**, boosting feature iteration speed by 35%.
- **Cross-Platform SDK:** Architected a unified **JSBridge SDK** for H5, powering key functions including Live Detection and OCR for loan onboarding. Ensured 100% UI consistency across these functions and a 40% gain in development efficiency.
- **Performance Optimization:** Optimised First Contentful Paint (FCP) through bundle analysis, code splitting, and tree shaking. Cut initial load time by 40% with Service Workers and HTTP caching.
- **Infrastructure:** Built a Node.js production monitoring system with real-time error tracking and anomaly detection on key platform metrics, reducing MTTR by 60%.
- **Component Library:** Standardised and scaled a shared **React**/**SCSS** design system across 5+ core products, streamlining design-to-code delivery and adoption.
- **Mentorship:** Mentored 5+ junior-to-mid developers and established a standardised front-end workflow encompassing **RFCs**, **Code Reviews**, and automated CI/CD deployment.
- **Platform Delivery:** Directed a team to ship Volcengine's Multi-Cloud Kubernetes Cluster Management PaaS product within 6 months. Designed a multi-tenant, micro-frontend app with a full **GraphQL/Apollo** stack across public, private, and hybrid cloud. This lowered dashboard latency and eliminated redundant REST calls.

### Xiaomi
_Front-end Engineer_

📅 Apr 2016 – Apr 2019

- **React Native Apps:** Core developer for Xiaomi's iOS and Android e-commerce apps in **React Native**, structuring core modules including Product Details, Reviews, and Order Lists. Maintained native-level performance and consistent UI across platforms.
- **Campaign Engineering:** Engineered a reusable game-template system for Xiaomi promotions using **React** and CSS animations, featuring interactive mechanics such as falling-packet clicks and card-flip reveals for voucher redemption. Reused across every high-traffic campaign, tuned for performance at scale.
- **Internal Platform:** Delivered an internal platform for the Product and Marketing teams. Digital operations specialists used it to manage product listings, campaign content, price adjustments, and marketing campaign configurations.

## 🎓 Education

### Beijing University of Posts and Telecommunications (BUPT)
_Recognised internationally as a top institution for computer science research._

- **Master of Software Engineering** · 📅 Sep 2013 – Mar 2016
- **Bachelor of Software Engineering** · 📅 Sep 2009 – Jul 2013

## 🌐 Languages

English (Fluent) | Mandarin Chinese (Native)

## 🔋 The Career Break (Aug 2023 – Mar 2026)

After 7 years of high-intensity work, I took a planned break to relocate to New Zealand and invest in things that don't fit in a sprint.

### 🗺️ Phase I: Stepping Back

- **Family time:** 👨‍👩‍👧 Reconnected with parents and family after years of working in another city.
- **Physical training:** Daily Ballet and Weightlifting 🩰🏋️ - focus and strength to carry back into the work.
- **Travel:** Lived and worked across cities in China (Chengdu, Dali, Xi'an, Guangzhou, and unique gems like Shunde, Miyi, Baoshan, Tengchong, Mangshi, and Tongchuan), and explored South Korea, Thailand, Indonesia, and Singapore.

### 🗣️ Phase II: Sharpening Up

- **English fluency:** **IELTS 7.5** (perfect 9.0 in Listening & Reading) and **PTE 83**.
- **Modern frontend:** Deep dives into React 19, WebAssembly, and performance tuning.
- **Shipping with AI:** Used Claude Design and Claude Code to build [Everyone Chess](https://everyone-chess.vercel.app/) end-to-end: design, code, and deployment, with AI as my pair-programmer.

### 🚀 Ready for the Next Challenge

Sharper focus, a clearer sense of the work I want to do next, and a lot of energy to bring to it.

---

## 📮 Get In Touch

> "Life is not a problem to be solved, but an experience to be had."

Looking for my next thing. Whether it's coffee, code, or just a hello, I'd love to hear from you.

**📧 Email**: {{< email user="robinyang029" domain="gmail.com" >}}

[🐙 GitHub](https://github.com/yrbing) | [📥 Download Resume (PDF)](/Robin_Yang_CV.pdf)
