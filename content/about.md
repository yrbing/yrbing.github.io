---
title: 'About Me & Resume'
layout: 'page'
---

{{< wordcloud dataSource="skills" >}}

**Hi, I'm Robin 👋**

I'm a **Senior Front-end Engineer** with 7+ years of experience. What I love most about this craft is using technology to bring a little more joy, ease, warmth, and delight into people's lives.

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

**Senior Front-end Engineer**  
📍 Auckland, New Zealand

## 🚀 Summary

Senior Front-end Engineer with **7+ years** of experience at global tech leaders including **ByteDance (TikTok)** and **Xiaomi**. **5 of those years** were spent building hybrid mobile applications across mobile web/H5, WeChat mini-apps, and React Native. Specialise in architecting high-performance web applications across the **React ecosystem**, with a strong focus on seamless **UI/UX implementation** 🎨 and platform-scale delivery. Now based in **Auckland** and contributing locally through Auckland City Mission while seeking the next senior role in New Zealand's tech sector.

## 🛠 Technical Skills

- **Languages:** TypeScript, JavaScript (ES6+), HTML5, CSS3 (SCSS, Tailwind CSS, styled-components)
- **Frameworks & Libraries:** React (Hooks, Context, Router), Next.js, Redux, Zustand, TanStack Query
- **Engineering & DevOps:** Webpack, Vite, CI/CD (GitLab CI/CD, GitHub Actions), Git Flow, Jest, Docker
- **Performance:** Core Web Vitals, Chrome DevTools, Bundle Optimization, Code Splitting
- **Cross-Platform & Mobile:** Hybrid App, JSBridge, React Native, WebView, Mobile Responsive Design
- **Backend & Collaboration:** Node.js, GraphQL, RESTful APIs, MongoDB, Express/Koa, WebSocket

## 💼 Professional Experience

### **Volunteer Software Engineer** | Auckland City Mission

_Mar 2026 – Present_ | [missiongrocer.co.nz](https://www.missiongrocer.co.nz/)

_Modernised Mission Grocer's Shopify e-commerce infrastructure (Liquid, custom JS/CSS, Shopify CLI), driving end-to-end digital transformation._

- **Cross-functional Strategy:** Partnered with the Project Manager in weekly strategy sessions, translating community needs into technical solutions and resolving operational bottlenecks.
- **Engineering Workflow:** Established the organisation's first engineering workflow from scratch, introducing a structured Dev-Review-Release lifecycle with reliable rollback strategies to ensure zero production downtime.
- **AI-Assisted Delivery:** Leveraged AI-assisted development tools, including **Claude Design** and **Claude Code**, to accelerate feature delivery and maintain code quality.
- **Information Architecture:** Identified a gap in the initial site architecture; proposed, designed, and shipped the About Us, Meet the Team, and FAQ pages to build local community trust and transparency.
- **CRM Migration:** Migrated legacy customer data to Shopify Admin CRM, eliminating manual email collection bottlenecks and unlocking data-driven, personalised lifecycle marketing campaigns.

### **Senior Front-end Engineer** | ByteDance

_Aug 2022 – Aug 2023_

_Led front-end architecture, UI/UX strategy, and system delivery for Volcengine's enterprise-grade PaaS product, the **Distributed Cloud Native Platform (DCP)**, commercialising ByteDance's cloud-native infrastructure for global B2B clients._

- **Architecture Leadership:** Appointed Front-end Lead for the DCP Proof of Concept; architected a unified, multi-tenant enterprise management console using **React**, **TypeScript**, and **Node.js**.
- **GraphQL Stack:** Designed the full GraphQL stack, including a Node.js/Apollo Server gateway that aggregates multi-tenant infrastructure metrics across backend services and an Apollo Client cache layer on the front end, cutting dashboard load latency and eliminating redundant REST round-trips.
- **Multi-Cloud Delivery:** Built adaptable front-end interfaces supporting public, private, and hybrid cloud deployment models, integrating cleanly with backend CI/CD pipelines.

_Apr 2019 – Aug 2022_

_Led front-end engineering for Douyin Consumer Finance's in-app hybrid experience (WebView inside the Douyin native shell), serving **10M+ DAU**._

- **Cross-Platform SDK:** Architected a unified **JSBridge SDK** for H5, ensuring 100% UI consistency in key functions and a 40% gain in development efficiency.
- **Architecture Migration:** Spearheaded the legacy migration from **Vue.js** to **React + TypeScript**, boosting feature iteration speed by 35%.
- **Performance Optimization:** Optimised First Contentful Paint (FCP) through bundle analysis, code splitting, and tree shaking; combined with Service Workers and HTTP caching to cut initial load time by 40%.
- **Infrastructure:** Built a Node.js production monitoring system with real-time error tracking and anomaly detection on key platform metrics, reducing MTTR by 60%.
- **Standardisation:** Architected a centralised internal **UI library** in React and SCSS, translating high-fidelity Figma designs into reusable components and ensuring design consistency across 5+ core products.
- **Team Leadership:** Mentored 5+ junior-to-mid developers and established a standardised end-to-end front-end workflow encompassing **RFCs**, **Code Reviews**, and automated CI/CD deployment; consistently earned top-tier performance ratings.

### **Front-end Engineer** | Xiaomi (Beijing)

_Apr 2016 – Apr 2019_

- **Cloud Infrastructure:** Core developer for **Xiaomi EcoCloud**, delivering critical management tools and modernising legacy front-end architectures for a B2B cloud computing platform tailored to Xiaomi ecosystem companies.
- **Architecture Modernisation:** Led the structural transition from **AngularJS** to **React**, implementing modular patterns and refactoring core architectures to reduce long-term maintenance overhead; upgraded the build pipeline from Gulp to **Webpack**.
- **React Native Apps:** Core developer for **Xiaomi Youpin's** iOS and Android apps in **React Native**; architected core modules including Product Details, Reviews, and Order Lists, delivering native-level performance and consistent UI across platforms.
- **Mini-Apps:** Engineered lightweight cross-platform mini-apps (WeChat's in-app application ecosystem) using **Taro**, building high-traffic e-commerce campaign pages optimised for fast load and conversion.

## 🎓 Education

**Beijing University of Posts and Telecommunications (BUPT)**

- **Master of Software Engineering**
- **Bachelor of Software Engineering**

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
