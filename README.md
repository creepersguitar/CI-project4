# CI-project4

Welcome to bite bait. A website designed to act as a booking system for a restaurant called bite bait.

View bite bait [here!](https://ci-project4-django-c7dcfccbb88c.herokuapp.com/)

## contents
1. [Design](#design)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Code Structure](#structure)
6. [UX](#ux)
7. [Testing](#testing)
8. [Bugs](#bugs)
9. [Deployment](#deployment)
10. [User Stories](#user-stories)
11. [Unfinished parts](#unfinished-parts)
12. [Sources and credits](#sources-and-credits)
13. [Contributing](#contribute)
14. [Contact](#contact)
## Design
Bite bait was designed as a booking system for a restaurant to streamline their booking process.
### Wireframe Design
The wireframe design was done via [wireframe.cc](https://wireframe.cc/)
![Wireframe-view](backgroundcode/static/backgroundcode/images/readme-images/wireframe-main.png)
### ERD Design
The Entity Relationship Design was done via [dbdiagram.io](https://dbdiagram.io/home)
![image](backgroundcode/static/backgroundcode/images/readme-images/ERD_overview.png)
To explain the image.
 - One user can have many bookings
 - One user can have many profiles (if they forget their email, lost their email etc.)
## Features
This section talks about the future features and features i have not had a chance to implement.
### Future features
Some of the potential future features i would like to include:
 - Ability to cancel reservations
 - Ability to add extra information i.e. allergies, dietry requirements etc.
 - Ability to see the menu of bite bait
 - Ability to edit the booking (change amount of guests or time)
 - Ability to delete their account
### unadded features
Some of the unadded features i have not had enough time to implement:
- Styling for login
- Styling for logout
- Styling for signup
- Confirmation popup for when user made a booking
## Installation
- This section details the basic views of how to install the different parts of the application such as django, gunicorn and the PostgresSQL database.
### Install Django
- To install Django, you first have to open your IDE (this will be shown in gitpod)
- Then you click on the [terminal](backgroundcode/static/backgroundcode/images/terminal.png)
    - or you click on the 3 bars in the top left hand of the screen
    - Then you click on terminal
    - finally new terminal
- Once you are in the terminal you type "pip3 install Djang~=4.2.1"
- Click enter then you will have Django installed
### Install PostgresSQL Database
**This is for current Code institute Students only!**
- The Postgres database can be installed for Code Institute Students only by heading to this [link](https://dbs.ci-dbs.net/)
- Then inputting the email you use to sign into the LMS (Dashboard) on Code Institute (CI)
- Then you should recieve an email saying the database is created as well as the details for it
- Finally you can add it to your project the same way as when ElephantSQL was working
### Install packages
 - To install the required packages you open the terminal
 - Then you type pip3 install <Name> (<name> is name of package)
 - If you need a required version you can type in the version after the name of the package (Like 20.1.0 for gunicorn)
## Usage
To make a booking,
1. Open the website
2. if you have not already you should sign in or signup
3. If you have already signed in you click on create booking
4. You then enter your details,
5. You then click submit
6. You should see a popup to say "Booking made!"
## Code Structure
- This section details as to how the code is structured and how to get this structure.
### Make structure
- To make this Structure, you first have to install [Django](#installation)
    - Then you type into the terminal "pip3 freeze local > requirements.txt"
- After that you type into the terminal "django-admin startproject codestar ." (Replace codestar with the name of your project)
- You then create the new app by typing into the terminal "python3 manage.py startapp blog"
- Then under codestar (the project name) you open up settings.py
    - Then you append 'blog', into the bottom of the installed apps list
    - Afterwards in views.py you need to type in "from django.http import HttpResponse" then "def my_blog(request): return HttpResponse("Hello, Blog!")" This is used as a test to make sure the project works.
    - In codestar/urls.py, you then have to type "from blog.views import my_blog"
    - There should be a bit of the urls.py called urlpatterns, in there you append "path('blog/', my_blog, name='blog'),"
- Then you can check the project runs by typing "python manage.py runserver"
    - open the preview in a new tab then append /blog to the end of the url
- If you have completed all of the above, then you should see "Hello, Blog!" on your screen.
### How code is structured
## UX
## Testing
 This Section is all about the testing of Bite bait. From testing that they work on different browsers to manual and automated testing.
### Browser testing
### Manual Testing
### Automated Testing
## Bugs
 This section is all about the annoying bugs which i either did fix or i did not have enough time to fix.
### Unfixed Bugs
### Fixed Bugs
## Deployment
## User Stories
This section is about making user stories and just in general talking about them.
### Make user stories

### Talk about user stories
## unfinished parts
This section is to talk about the parts of bite bait i have built but not had time to test as well as link back to the main part.
## Sources and Credits
 This section is all about the help i got from links, people, my mentor as well as the links to what i used to help my project.
### Sources
- The fonts were generated by google [fonts](https://fonts.google.com/)
- The main structure of the code was followed from Code Institutes I think therefore i blog module on their 5 project course.
- Code institutes github account who i checked my code with when i thought i missed a [step.](https://github.com/Code-Institute-Solutions/blog)
- Youtube for when i had an error 500 and a heroku h10 error.
    - h10 error [video!](https://youtu.be/68iCwSmSIvA?si=1ZuDBlHXPwnbr9Au)
- Unsplash for the main photo for [bite bait](https://unsplash.com/photos/brown-and-gray-concrete-store-nmpW_WwwVSc)
### Credits
 - My mentor Spencer Barribal for always providing advice and improvements that i can add to Bite bait
 - One of my old college projects for being a reliable source of information and reminding me on how to do certain parts of the design (like the entity relationship diagrams) aswell as part of the development in python.
 - My fellow peers and friends for giving me the motivation to finish this project when i have suffered with imposter syndrome
 - John from the code institute Tutor team for helping me solve an issue with error 500.
 - Other coworkers/ residents where i work at supporting me in getting this project done
## Contributing
Contributions are welcome! If you would like to contribute to this project, please follow these steps:
 - when i say feature i mean what you are calling your branch (step 2), and what you are commiting aswell as pushing (steps 4 and 5)
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature/YourFeature`).
6. Open a pull request.
7. Wait for pull request to be looked at by me.
8. If its okay then i'll approve it but if there is any potential improvements then i'll comment on it.
## Contact
 - If you have any suggestions or questions then feel free to reach out
 [Github](https://www.github.com/creepersguitar)
 [LinkedIn](https://www.linkedin.com/in/george-small-055151204)