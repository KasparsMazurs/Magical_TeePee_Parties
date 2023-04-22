![MTP logo](https://lh3.googleusercontent.com/pw/AJFCJaWpEdbcTvo5v-yvBWJEXHG-zWzH8mVsn8HppyR9T7QYm9keK6uwV58rzUaNyrog8iuh8xqSvex-vj1tQRSAE88Gq0hkHBr9IJEfNia6WsFaAbYgpCHVLxjxhrizVmqAyd_80FkRt0eGl93Q0mzpq__CPA=w125-h125-s-no?authuser=0)

# Magical TeePee Parties

View the repository in GitHub <a href="https://github.com/KasparsMazurs/Magical_TeePee_Parties" target="_blank">here</a>

View the live project <a href="https://magical-teepee-parties.herokuapp.com/" target="_blank">here</a>

## User Experience

### Goals

The purpose of this website is to showcase a rental company called 'Magical TeePee Parties' that offers remarkable and enchanting experiences for events such as children's sleepovers and birthday parties. The website enables potential clients to view the prices, images, and blog posts related to kids' parties, and make party bookings.

### Planning

A significant amount of effort went into the planning phase to determine the layout and structure of the agile board. Following a solo meeting where I switched between the roles of product owner, user, and developer, it was decided that Github projects would serve as the ideal agile tool for the Magical TeePee Parties PP4 project. With only limited time remaining until the project deadline, it was decided to break the development process into four iterations, each lasting one week.

Once the project's scope was clearly defined, I proceeded to create milestones and epics to help organize the development process. User stories and tasks were added to the backlog and prioritized using the M.o.S.C.o.W prioritization technique. Afterwards, each task was assigned to the appropriate milestone and iteration.

### Epics and User Stories

### Epic: Create initial Django Setup

- Tasks: Install Django and dependencies (libraries) #4

    -	Install Django
    -	Install libraries
    -	Create a requirements.txt file
    -	Create the project
    -	Create the app
    -	Make database migration
    -	Test locally in the browser to confirm successful Django installation

-	Issue: Early deployment to Heroku #5

    -	Task 1 - Create Heroku app
    -	Task 2 - Attach the PosgreSQL database to the Heroku app
    -	Task 3 - Prepare environment and settings.py files
    -	Task 4 - Add new SECRET_KEY to settings.py and to Heroku
    -	Task 5 - Connect PosgreSQL database in the settings.py
    -	Task 6 - Make database migration
    -	Task 7 - Disable STATIC_ROOT on Heroku by adding DISABLE_COLLECTSTATIC=1 to Config Vars
    -	Task 8 - Add Procfile

### Epic: Create App and pages

**USER STORY: Approve partie**

As a **Site Admin** I can **Approve or disapprove party's date** so that **I can manage availabilities**

**USER STORY: Book a Partie**

As a **Site User** I can **Book a party** so that **I can Book a party onlin**

**USER STORY: Approve comments**

As a **Site Admin** I can **approve or disapprove comments** so that **I can filter out objectionable comments**

**USER STORY: Manage posts**

As a **Site Admin** I can **create, update and delete posts** so that **I can manage my blog content**

**USER STORY: Like**

As a **Site User** I can **like a comment on a post** so that **I can interact with the content**

**USER STORY: Comment on a post**

As a **Site User** I can **leave comments on a post** so that **I can be involved in the conversation**

**USER STORY: Account registration**

As a **Site User**, I can **register an account** so that **I can comment and book a party**

**USER STORY: View comments**

As a Site **User / Admin,** I can **view comments on an individual post** so that **I can read the conversation**

**USER STORY: View likes**

As a **Site User / Admin**, I can **view the number of likes on each comment** so that **I can see which is the most popular or viral**

**USER STORY: Open a post**

As a **Site User** I **can click on a post** so that **I can read the full-text**

### Epic: Testing and Deployment

**USER STORY: Website works as intended**

### Epic: Documentation

**USER STORY: Complete readme documentation**

## Features












1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.


## FAQ about the uptime script

- An ID that is randomly generated each time the workspace is started.

**Anything more?**

`uptime.sh`
