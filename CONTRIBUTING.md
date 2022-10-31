# Contributing to Alice Game

## Code of Conduct

Be nice
Be supportive
Give constructive feedback
Check your ego
Have fun with other new devs!

This is an harassment free space. We support and require the same code of conduct that wonderful repos like Gatsby have. 
[Gatsby code of conduct](https://www.gatsbyjs.com/contributing/#code-of-conduct)
**"In the interest of fostering an open and welcoming environment, we as contributors and maintainers pledge to make participation in our project and our community a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, gender identity and expression, level of experience, nationality, personal appearance, race, religion, or sexual identity and orientation."** 



## How to contribute:

This is a project for new devs wanting to learn open source web development and version control (github) with others. The first step is to introduce yourself in the discussions tab. Please answer the following quick questions. 


1. What is your real first name and Github profile link?
2. Where in the world are you (country and time zone)?
3. Where are you in your learning journey? -> Just learning html, know html and css, just started learning javascript, comforatble with more advanced javascript such as promises, api, etc.?
5. How are you learning? -> Self taught, bootcamp, computer science courses
6. What would you like to work on in this repo


## Limit to the Initial Number of Contributors
As this is the first time I'm maintaining an open source repo, I'm limiting the inital number of contributors to 10 so I can keep up with the PRs and time required. If we've reached 10 contributors, I'll look at having a co-maintainer so we can add more contributors.

## Read the Hacktoberfest Rules

These apply even after Hacktoberfest is over.
[Hacktoberfest Rules](https://hacktoberfest.com/participation/#contributors)


_____


# File Name Conventions

## HTML elements - Ids and Classes

Ids and Classes for HTML elements should be named in lower case with '-' in between words. For example:
      `<div class="player-choice-radios" id="player-choice-radios">
				<div class="player-choice-radios">
					<input 
					type="radio"
					id="drink"
					value="drink"
					name="player-choice-radios"
					>
					<label for="drink">Take a Drink</label>
				</div>`
        
## Javascript Variables

Javascript variables should be the camel case of their associated html ids

for example:
`const playerChoiceRadios = document.getElementById('player-choice-radios')`
