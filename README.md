## **Summer 2023: What's Happening with The Alice in Wonderland Project?**

[Update on https://gingerkiwi.blog](https://gingerkiwi.blog/blog/2023-04-03-whats-happening-with-the-alice-in-wonderland-project)

The Alice in Wonderland Project started a lot of enthusiasm, but without much planning during Hacktoberfest 2022. Getting involved in open source and learning GitHub workflows can be intimidating and challenging for new developers. So I created an open source repo to help other new developers learn GitHub work flows, learn how to contribute to a remote team project, get involved with open source while being social and making something fun.

However, I've since realized that I was actually creating something more than an open source project. It's the fledgling curriculum of a project based learning program. I stopped teaching in 2019, but I guess I've never actually stopped being a teacher. The best way to accomplish the goals of the project are to take a pause, reflect, and start over using my teacher skills to create a comprehensive experiential, project based learning curriculum.

So instead of just building something as we go, I'm going to have to:

- completely build out the project in a private repo
- create a new public repo so we can start fresh
- pre-plan the steps in building the project
- develop onboarding
- figure out roles, responsibilities, and how many devs are ideal at once
- create lesson plans, and written and/or video lessons
- find one or more experienced devs that would be willing to serve as mentors/maintainers on different parts of the project (eg, html, css, js)
- create a landing page and signup form
- most likely create a discord community to allow video chat, screen sharing, and a place for longer discussions. The challenge will be to be clear about what discussions belong on discord, and what should be part of the GitHub repo.

I'm aiming to have things ready for September so we're ready for the influx of people during Hacktoberfest 2023.

**December 06, 2022**

After a whirlwind busy November, I'm back maintaining this project. I've finally learned how to manage an open source repo in VSCode on my local MacBook, so I can help others and have an organized project. Over this week I'll be publishing some step-by-step guidelines for beginners on how to create, name, and work with branches so we can all keep the Alice in Wonderland Project organized.

You'll notice that I've moved most of the .md (markdown) files into their own new directory "Documentation". That makes our main file list easier to read, and should make the resources easier to find too.

*If you want to be ahead of the game when we start posting more issues, have a read and even try to follow along with this awesome, recent article while you're waiting.
[Create Your First Github Project in VSCode. By Jean-Christophe Chouinard, 12 October 2022](https://www.jcchouinard.com/create-your-first-github-project-in-vscode/ )*

**Thank you to everyone who contributed during Hacktoberfest! <br>
Happy Coding, and Welcome to Wonderland! <br>
Liz, GingerKiwi**
___

# **About**

*Welcome to Wonderland!*
The Alice in Wonderland Project is a html/css/vanilla javascript text-based game with an Alice in Wonderland theme. 

This is a repo geared towards new web devs who are learning open source and want to work and socialize with other devs. That includes the maintainer(s)! Most issues and PRs are small. To keep things managable, I'm limiting the contributors to 10 for now. Quality over quantity. 

**If You'd Like to Contribute Please Follow These Three Steps:**
1. Please introduce yourself in the [discussions tab](https://github.com/GingerKiwi/alice-game/discussions/4)
2. Have a quick read through the CONTRIBUTING.md and README.md files
3. Comment in the issue that you'd like to work on.

If we still have contributor spots open I'll assign the issue.

A great example of a text-based game is the classic [Oregon Trail](https://www.smithsonianmag.com/innovation/how-you-wound-playing-em-oregon-trailem-computer-class-180959851). 
Alice will have much better font and graphics, but will still be text-based without animated elements.

## Alice Game Background

This game was orignally created as a python console game as part of a computer science course at Massey University, New Zealand in 2020. Part of the assignment was documenting the thought process using comments. (So there's a lot of comments in the .py file!). The assignment was the classic [Camel game](http://programarcadegames.com/index.php?lang=en&chapter=lab_camel) from "Program Arcade Games and With Python And Pygame" and orginally concevied in 1979 in "More BASIC Computer Games".

However, the premise of the game is both racist and colonlialist - stealing an camel from the "natives" and racing away from them across the Mobi desert. So I changed the theme to Alice from Tim Burton's Alice in Wonderland movie rescuing the Red Queen's Bandersnatch from his imprissionment and racing across Underland to get to the White Queen's castle. I also added a random chance that the player would be attacked by the Jabberwocky, be killed, and the Jabberwocky poem would print on the screen.

## From Python Console to Javascript Text Based Web App

The goal is to take the existing python code and turn it into an accessible text based web game in html, css, and vanilla javascript. The game type is much like the classic text based "Oregon Trail" PC game.

### Repo Started with Minimal Code

The repo is being started with only a small amount of code and the app will not be functional. Instead comments have been added in the project files to show where code blocks should go and what they should do. The point is to collaborate in changing the orginal python file into a fun, working, and accessible web game.

## Supporting Other New Devs Learning Open Source & GitHub

In 2022, I participated in my first Hacktoberfest and Hacksquad while in the Scrimba Frontend Developer Career Path. Starting in open source can be intimidating! Turning this Alice python game into a vanilla javascript text based game web app could be a fun way for new devs like myself to collaborate and learn how to work on an open source project together. 

Version control was completely lacking from the unviersity courses I took in 2020-2021, so maintaining an open source repo geared towards new devs seems a good social way to learn and contrinute to the open source community. I know I will make mistakes (likely many), but that's a good way to learn. I hope others working on this project will bear with me while I learn how to maintain an open source repo.

### Intentionally Small Issues and Pull Requests

Given that this is a repo for us new devs to learn together, I'm aiming for the issues and the PRs that solve them to be small and doable for first time web devs. These can be as simple as adding a single heading and text, a short basic vanilla javascript function, or changing the colour variable in the CSS. This makes contributing to open source accessible for really new devs that are just learning the basics of html and/or markdown, as well as those of us that know more advanced css and javascript.

## Accessibility - Part of Every PR - Not Retrofitted and Refactored

This project is being developed with accessibility in mind from the beginning and at every step. That starts with sematic html, labelling elements, and having a "skip to main content". It also means that even if planned accessibilty features such as theme switching aren't being released in a particular version, the code is still written to make those features easily added.

This is one reason why CSS variables are being used, instead of hard coding colours and font/text attributes. While CSS variables are a more intermediate level skill, they make it easier to switch colours, type/font and implement theme switching instead of having to refactor the entire stylesheet.
