---
date: '2026-06-26T00:00:00+12:00'
draft: false
title: 'How I Find the Work That Actually Matters as a Volunteer Developer'
tags: ['Shopify', 'Volunteering', 'Career', 'Marketing']
categories: ['Career']

cover:
  image: 'images/screenshot-missiongrocer-about.png'
  alt: 'Mission Grocer About Us page'
---

In my last article, I talked about how, as the only IT person around, you've got to think outside the box. Don't just get stuck fixing pages and bugs. Go find out what people actually want and what the team needs, then figure out what you can do about it.

Now I'd love to walk you through how I go about finding those needs.

## First Meeting, First List

When I first started volunteering with Mission Grocer, they honestly hadn't planned on having a developer around. Their website wasn't a big priority yet, so honestly, nobody quite knew what to do with me.

So I just took the lead myself. Before we even met in person, I'd already been poking around their website, jotting down a list of things I figured I could fix. Things like accessibility fixes, better user interactions, a mobile-friendly layout, a proper square favicon, an announcement bar, all pretty trivial stuff.

That list turned out to be just the start of what I'm doing now, but it got the conversation going, and gave us a shared starting point for figuring out what they actually needed.

## The Weekly Check-in

A developer role can be fully remote, but honestly, I don't think you can do good tech work without understanding the people and the mission behind it. So I suggested a weekly check-in. That little meeting quickly became the most important part of my whole workflow.

![Example of a Weekly Update email, summarizing what was completed, what's in progress, and discussion points for the upcoming check-in](images/weekly-update-example.png)

Every Wednesday, I send a Weekly Update email first, then we sit down face-to-face to walk through what I did the week before and what's coming up next. I'll also bring up a couple of things I want to chat about. More importantly, I ask. I ask the manager, and sometimes other staff, what's bothering them, what they're hoping for, what's on their minds.

Over time, I've built up a real picture of what the team does day to day and what they're actually trying to achieve. That's what makes the difference. The work I build isn't just there to keep myself satisfied. It actually connects to what they're trying to do.

## What to Listen For, With the Team

One thing I've learned is to listen for the spark moments in those conversations, the moments where a developer's skills could really make someone's life easier.

In one of our early check-ins, my manager mentioned they'd had a stall at a market a few days before. I asked how they let people find out more about Mission Grocer and join the food community. Turned out it was flyers and and questionnaires.

That felt like something worth fixing. If someone walks past the stand and wants to know more, there should be an easier way to do that than asking a staff member, filling out a paper form, or searching for Mission Grocer online.

There's something warm about doing it the traditional way, chatting with a staff member or filling out a form by hand. But these days, having a digital option too just makes things easier. A QR code that leads somewhere useful could change that whole moment.

Soon we had QR codes popping up everywhere: the front window of the store, the inside cover of the recipe book, even tabletop standees at events. Each one needed its own link with its own UTM parameters, and I realized we badly needed a tool for this. So I built a simple tool page for the team, where anyone can grab a link or a QR code for whichever page they need, whether that's for a market stall, a flyer, or a social media post.

![Mission Grocer's tool page for generating a campaign URL and QR code for each page](images/screenshot-tools.png)

## The People Who Come Here Matter a Lot

Besides listening to the team, listening to the people who come here matters just as much, too.

I've also picked up a few shifts at the store myself, chatting with people and watching what they need, which produce is most popular, what they actually want to know about Mission Grocer.

People sometimes look for the store address through our website or Instagram, so instead of just listing addresses on the homepage or Instagram profile, I built a page with a map link for each location and opening hours.

![Mission Grocer's Visit Us in-store page showing store hours and addresses for the HomeGround store and the Albert Park pop-up](images/screenshot-missiongrocer-visit.png)

Some people are interested in volunteering here too, so we built a Meet the Team page with intros for all the staff and volunteers, plus a way to apply.

![Mission Grocer's Meet the Team page, titled "The faces behind the fruit bag," with photos of staff and volunteers at the HomeGround and Albert Park locations](images/screenshot-missiongrocer-team.png)

I even found people on Reddit who weren't sure whether Mission Grocer was for everyone, which is why we built the FAQ, About, and Contact pages.

![Mission Grocer's About Us page with the headline "A neighbourhood grocer with community at its heart" and a short description of the shop's mission](images/screenshot-missiongrocer-about.png)

## Getting the Word Out Online

Mission Grocer is built on the idea that good food belongs to everyone. Every purchase, and every "pay it forward" at the till, help keep healthy food accessible for the people who need it most.

Getting the word out online matters a lot these days, especially for helping more people find and join the food community. We've had an Instagram account posting fresh produce every week, which is a good start. From there, I first looked into Instagram Shopping, a feature that lets you set up a shop right on your Instagram profile and tag products in posts and stories.

Unfortunately, after a bit of research, I found out it's not available in NZ. So I shifted focus and took a closer look at the Instagram profile instead. The bio link pointed straight to the homepage, and the homepage didn't really do much with that visit. It didn't explain their mission, introduce the team, or show where the stores were.

What made a lot more sense was a mobile-first "link in bio" page. It's a compact page that covers who we are, what we stand for, who's behind it, and where to find the stores. Before, we'd been cramming all of that into the profile bio itself, which is tiny and kind of a pain to update. Now there's a dedicated page that actually does the job, and it's easy to keep up to date.

![Mobile-first link-in-bio page for Mission Grocer's Instagram, listing buttons for the Auckland Food Show, ordering a fruit box, visiting in-store, shopping online, gifting a Pay It Forward bag, and more](images/screenshot-missiongrocer-bio.png)

## Building Infrastructure for Events

Mission Grocer has two physical stores, and they often get the chance to show up at special markets and events.

It's worth building something specifically for those offline, face-to-face events, things like a landing page to promote the stall beforehand, a QR code sign-up at the table, and a thank-you email with photos from the day.

My first real opportunity to do this is the Auckland Food Show coming up in July. Mission Grocer has a stand there, so we'll finally get to see if meeting someone in person carries over online.

The idea is simple:

Before the event, we build a landing page to promote the stall, and add an Instagram countdown or story tag to build interest before people even show up in person.

At the event, people scan a QR code at the stand and land on a page inviting them to join the food community. To make sure people actually notice it, we also make a printed sign with the QR code that sits right at the front of the stall. When people join, they get a friendly welcome email with a discount or gift as a thank-you, and hopefully, we'll hear from them again down the road.

After each event, we send out a thank-you email with photos from the day, and maybe a short feedback survey too, so we can hear directly from people about how it went.

To sum up, apart from the traditional flyers and questionnaires, this time we'll be able to build a real, lasting connection with people. We can track which event someone came from, reach out to them based on what they need, and get a sense of how much each event actually helped.

## The Pattern

Both of these ideas came out of a single, ordinary meeting. That's the pattern I've come to rely on: spot the gap, then figure out the simplest thing that closes it. The weekly check-in is what makes that possible. Without it, I'd just be guessing at what the team needs, and the work would drift away from what actually matters.
