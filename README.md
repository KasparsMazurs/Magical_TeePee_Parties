![MTP Logo](https://lh3.googleusercontent.com/pw/AJFCJaXR51mMd6teY8KzLldeNL-_-kLlh4viaFTkoGFrPvnVzNKtn1_HV4MYm8FPIhBT4iMlgMJapYgF5CgAA_I8QfFgB3QMjaPdBfM-Zf5uJoGBW8X-ppZSP7n9ODnDVuKiU2zSzzUn6mnN_Z8KaXaUcjTiYw=w125-h125-s-no?authuser=0)

# Magical TeePee Parties

![MTP Am I responsive image](https://lh3.googleusercontent.com/pw/AJFCJaWmXF_lzbBWX8l8aH6tpZSVDSuavlw9TIj5-jnMccXbhzOHKHkyuWr-NkIiL2-5r0179b5sgvpn10DoQeCVgEKEryLiuWq6ggcCti7B2Ygf43FQ0u11ui8MjwjdOtb7GAYMifQdXBC8y8Mttq9xmuUm4A=w1657-h1024-s-no?authuser=0)

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

### **Existing Features**

**Header & Navigation**

The Header & Navigation section comprises of three distinct sections that users can interact with. 
- The first section, which is the Logo section, displays the logo of Magical TeePee Parties. By clicking on this section, users can easily navigate back to the Home page. 
- The second section, referred to as the Navigation bar, allows users to access the Home page. If the site is accessed on a mobile device, the Navigation bar will be replaced with a collapsible button. 
- The final section, Authorization, enables users to navigate to the login or registration page. If users are already logged in, the options will be updated to display a personalized greeting of "Welcome, user_name!" along with a sign-out button.

**Authorization**

This section displays the homepage for registered users who are logged in. For users who are not registered, they have the option to register and create an account.

**Footer**

This section displays the following information to users:

- COPYRIGHT

- Users can follow Magical TeePee Parties on Facebook, Instagram, or TikTok. By clicking on any of these icons, they will be redirected to the respective social media page in a new web browser tab.

- Users can also contact Magical TeePee Parties by accessing their phone number, email address, and physical address. Clicking on any of these options will open Google Maps in a new tab.

**Home**

The main page can be divided into two sections.

The first section features a prominent Jumbotron image with a call-to-action button that redirects users to the party booking section. 

The second section contains the Blog posts/News, which showcases news and updates related to kids' parties. Each post header is clickable and expands to reveal the full post. Additionally, users can view the post's date, image, and a brief introduction to the post in this section.

**Blog post**

Upon clicking a post, users will be redirected to its full content page, which features an associated image, header, date of publication, and the complete content. Moreover, users can react to the post by liking it and view the total count of likes received. They can also see all the comments that other users have left for the post and leave comments themselves.

**Like**

If a user is logged in, they can like a post by clicking on the like button. Upon clicking the button, the associated image will change color to indicate that the user has clicked the button, and the total likes count will increase by one. However, if a user is not logged in and clicks the like button, a message will appear informing them that they can only like the post if they are logged in.

**Comments**

The comment section is visible to all users, and it displays the name of the user who left the comment, the time it was left, and the comment itself. If a user is logged in, they can also leave a comment by accessing the comment form. The form has a welcoming header with the text "Leave a comment," and the user's name appears before the comment body. After writing the comment, the user can click the "submit" button, and a message will appear, saying "Your comment is awaiting approval." In the background, the site admin can approve the comment in the admin panel, and only after the admin approves the comment, other users can see it.

**Products**

This section displays all the products related to Magical Teepee Parties, with each product appearing in a separate block. The product blocks are displayed similarly to the blog/news posts.

**Products Description**

When a user clicks on a product, they will be able to view the product's header, content, and pictures associated with the product.

**Book party**

The homepage will be divided into three sections:

1. The price list section, where clients can view all the prices related to Magical Teepee Parties.
2. The "Book a Party" form is visible only to logged-in users. If a user is not logged in, they will see an explanation that they need to log in to submit a party request. The form requires the following information to be provided:

    - Party Theme - drop-down box
    - Extras - check box
    - Kids Age - drop-down box
    - Number of Teepees - drop-down box
    - Street - text field
    - City - text field
    - County - text field
    - Eircode - text field
    - Date - date field
    - Email - text field
    - Contact Number - text field
    - Additional Info - text field

When the user clicks on the submit button and provides all the required information, they will be redirected to the "Submitted Parties" section. Otherwise, they will be informed about the data they need to provide for submission.

3. A button that redirects to the "Submitted Parties" section.

**Submitted Parties**

This section is exclusively for logged-in users, where they can view all the parties they have submitted. Parties that are awaiting approval by the admin will be displayed in a yellow background. Users will be able to see all the information they have provided and will have the option to edit the information or cancel the party. Parties that have been approved by the admin will be displayed in a green background, and users will also see the price for the party. Users will be able to edit the party information, but they will not be able to cancel an approved party. If a user changes the party status, it will automatically change to "not approved."

**Edit party**

Users will have the ability to modify the information they provided for their party. If a party has already been approved and the information is edited, the party will automatically be changed to "not approved" and will need to wait for approval again.

**Cancel party**

Users will have the ability to cancel parties that have not yet been approved.

**Gallery**

In this section, users can view all galleries that are related to Magical Teepee Parties. Each gallery will be presented in its own block and displayed in a similar format to that of the blog/news posts.

**Open gallery**

When a user clicks on a gallery, they will be able to view all images related to that gallery along with a brief description.

**Contact us**

This section will provide users with the following information:

1. Contact Information - You can get in touch with us through various means such as phone, email, etc.
2. Social Media Links - You can follow us on our social media accounts.
3. Send an Email - This feature uses an API to directly send emails to Magical TeePee Parties' email address.
4. Location on Google Maps - You can locate Magical TeePee Parties' physical location on Google Maps.

**About us**

The mission, goals, and vision of Magical Teepee Parties are presented to the users.

## **Future Features**

- In the upcoming iteration, our users can expect to have access to three new features that we will be introducing. Four features aim to enhance the overall user experience and provide additional functionality to meet their needs. We are excited to bring these new additions to our platform and look forward to the positive impact they will have on our users.

- In the next iteration, a manual option for naming images will be added in the admin panel during image upload. Currently, each image is automatically given a name. This new feature will allow for more control and customization when it comes to naming and organizing images for the website.

- In our next iteration, we plan to improve the presentation of both product and gallery images, as the current display can appear cluttered and disorganized. By enhancing the visual experience of our website, we aim to improve the overall user experience and increase engagement with our products and services.

**Share**

Users will have the ability to directly share blog posts and galleries to their social media accounts.

**Images**

Users will have the ability to click on images found in both the product and gallery sections of the website. Once an image is clicked, it will expand and take up the entire screen, providing a better viewing experience. This feature will enhance user engagement with the website's content and improve the overall user experience.

**Like and comment**

Users will have the ability to engage with the content by leaving comments and liking both galleries and products. This feature encourages interaction and feedback, making the website more engaging and user-friendly. By leaving comments and likes, users can also help other potential customers to make informed decisions.

**Book party**

Users booking a party will have the advantage of seeing real-time availability, allowing them to plan and book accordingly. Additionally, the platform will provide users with approximate pricing information for the party before it is approved, giving them an idea of the potential cost. This feature will enable users to make informed decisions regarding their party bookings and ensure that they are within their budget. By providing real-time availability and pricing information, the platform will provide a user-friendly experience and a streamlined booking process for users.

## Design

### Wireframes

Balsamiq was utilized to create the wireframes, and great effort was invested in ensuring that the final website would appear and function precisely as specified in the wireframes.

![MTP wireframes](https://lh3.googleusercontent.com/pw/AJFCJaXOztKMVVvXojBuZBK3pqJ4hiF1pbzhubAR2pfyIrpic5d5yTdzX5c8V4gEoHCGL0mz2fV4vPK3kxJJPfvuS9TPpxakncBQ5h9kfv6l9ORBS2LTfQucWscz-Vrwvi2mtHd4JjxlLzbOnpuopkU0PARo6w=w905-h1324-s-no?authuser=0)

### Fonts

The website utilized Google fonts Alice and Playball to enhance the typography. The selection of these fonts was made to ensure the website's overall aesthetic and branding remain consistent. These fonts were chosen for their readability, clarity, and unique style.

## Testing

### Responsive Design

Regularly during development, Chrome Developer Tools was utilized to test the website's responsiveness on various screen sizes. The website's responsiveness was achieved through the use of Bootstrap 4 and CSS. The features section above demonstrates the website's responsiveness on different screen sizes.

### Validator Testing

**HTML**

Code passed official <a href="https://validator.w3.org/nu/?doc=https%3A%2F%2Fmagical-teepee-parties.herokuapp.com%2F">W3C Validator testing.</a> 

**CSS**

Css passed official <a href="https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fmagical-teepee-parties.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en">W3C Validator testing.</a> 

**Javascript**

The alert function was tested with <a href="https://jshint.com/">jshint.com.</a>

**Python**

The code was tested with PEPE8.

**Lighthouse**

Pages were tested with Chrome Developer Tools using the Lighthouse resource.

![MTP Lighthouse](https://lh3.googleusercontent.com/pw/AJFCJaVQ_MuU_EV5E2_xWcaQTEJN_WH6P4VNDnwb2eF5nn6vDiDcj3ncpDsaQPaPecmZ6Ma3bMT-xqHYd8ObwXfmTEjjHxVylDhPjFJeS8PX0cLd2YUPIRDci47HzSrTBa4DbsbxotE7kdj5QTPpNGprf0Ks5A=w1009-h620-s-no?authuser=0)

### **Functional Testing**

- Landing page (Homepage)

    - Clicking on the logo image will take the user to the homepage.
    - Pressing the button on the Jumbotron will redirect the user to the party booking section.
    - Clicking on a post will open the post details.

- Post delais

    - When the like button is clicked, the color of the button changes and the total number of likes increases.
    - If the user is not authorized and clicks the like button, a message appears.
    - All comments are visible.
    - When a user is logged in, they can leave a comment.
    - After a comment is submitted, the admin can see it in the admin panel and approve it.

- Footer

    - The links located in the footer function correctly as intended.

- Products

    - The list of products is visible
    - The links located in the products function correctly as intended.

- Product details

    - Product details and images of product are visible

- Book party

    - The link to "Submitted Parties" is functioning properly.
    - If the necessary information is not provided by the customer, a notification will be displayed.
    - When a party request is submitted, it can be viewed in the admin panel and the user will be redirected to the "Submitted Parties" page.

- Gallery

    - The list of gallerys is visible
    - The links located in the gallerys function correctly as intended.

- Gallery details

    - All images associated with the gallery are visible.

- Contact us

    - The email API is functioning correctly as intended.

- Login/Logout/Register pages

    - The account creation, login, and logout functionalities work without any issues for the user.

### Browser Testing

Pages behave as expected in all browsers tested. The website was tested in Chrome, Firefox, Brave Browser, Edge and Opera.

### Bugs

**Fixed Bugs**

- I encountered a booking error when attempting to book a party. The issue was due to a code segment that verifies party ID uniqueness by checking past bookings. However, since there were no previous bookings, the code was unable to generate a unique ID number, resulting in the error.

- All images in the galleries became visible in any of the galleries due to an error in the views.py file.

- There were cases where bookings were automatically approved.

**Unfixed Bugs**

The product description in the Products page contains a visible <p> tag.

## Deployment

Acting on the instructor's advice of "deploying early to avoid problems down the line," we chose to deploy our website to Heroku right after the initial setup. This helped us identify and address any issues early on, resulting in a smoother development process. Additionally, it allowed us to test the website's performance and make improvements before the final release.

### Heroku

The website was deployed to Heroku using several steps. 
- First, a Heroku account was created and a new app was created with an app name and region. 
- Heroku Postgres was added as a resource and configured with a hobby dev plan. 
- Config vars were added in the settings tab, including SECRET_KEY, DATABASE_URL, and CLOUDINARY_URL. 
- The deploy tab was selected, and Deployment method was set to GitHub. 
- The main branch was chosen for manual deployment, and the app was deployed. 
- Automatic Deploy can also be enabled for ease of use. If the build fails, the resources tab can be accessed to view the build log and find out why it failed and how to fix it.

### Version Control

Throughout the development process, version control was managed using Github. The team utilized the platform to collaborate and manage changes to the codebase. Each feature and bug fix was implemented on a separate branch, and changes were reviewed and merged into the main branch via pull requests.

## Technologies used

- HTML5 for the contents and structure of the website.
- CSS3 for the styling and animations.
- Cloudinary for static files and media.
- Summernote for posting/design blog/news post
- Balsamiq for wireframing.
- GitHub as a remote repository.
- gitpod.io was used as IDE and git version control.
- Heroku to deploy the website/app.
- Chrome, Firefox, Brave Browser, Edge and Opera for browser testing the responsiveness.
- Chrome Developer Tools for testing screen sizes and using Lighthouse.
- Favicon.io to create a favicon.
- Image converter for optimizing images
- Bootstrap 4 for responsive design
- emailjs API for emails

### Frameworks

- Django

## Credits

- Inspiration for news was taken from the Code Institute project "Blog"
- Stackoverflow for providing solutions for problems in code

## Lessons learned

- Need to use more Agile methodology to be more presist in results
- Blog / Gallery / Booking should be in separate apps