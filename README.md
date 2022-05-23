 <h1>Clever Birds: Embracing Your Children’s Passion for Video Games </h1>
 
 Clever Birds a project developed as an integration for a game via API along with Flask webserver. This project  is focused on the project management process of building our application. Throughout the development of this project, we used Confluence and Jira together for planning and coordinating our work. 
 
:arrow_forward: Duration : 3 months
<br>
:arrow_forward: Team : Teamwork of 4

> :round_pushpin: Goals: 
> * A light-weight demonstration of a working model of the web application Clever Birds and the description of testing. 
> * Apply Scrum project management methodology for organizing and managing our project. 
 
:clapper: Click [here](https://drive.google.com/file/d/1ey6QWLDuiZW_9KxYp4D29YSA3fxOb3vb/view?usp=sharing) to watch our video presentation 

 <h1>Table of Contents</h1>

<!-- TOC -->
- [1. Overview](#1-overview)
- [2. Requirements](#2-requirements) 
    - [2.1. Functional Requirements](#21-functional-requirements)
    - [2.2. Non-functional Requirements](#22-non-functional-requirements)
    - [2.3. High priority requirements](#23-high-priority-requirements)
- [3. How to use our platform](#3-how-to-use-our-platform)
- [4. Clever Birds Game](#4-clever-birds-game)
- [5. Project Architecture](#5-project-architecture)
   - [5.1. Activity Diagram](#51-activity-diagram)
   - [5.2. Project Structure](#51-project-structure)
- [8. Python Dependencies](#8-python-dependencies) 
- [9. Tools](#9-tools) 
- [10. Installation](#10-installation)
- [11. Confluence Documentation](#13-confluence-documentation)
- [12. Useful Links](#15-useful-links)


 

<!-- /TOC -->
 
## 1. Overview 

 Clever Birds a project developed as an integration for a game via API along with Flask webserver. The player navigates the avatar bird through obstacles without hitting them, earning points as he or she passes each pipe. The application has a chatbot named “Tweety”, who guides parents about how to use their children's game time as an educational experience. 
  
* [Project Charter)(https://github.com/SEPM-2022/CleverBirds/blob/develop/assets/NewProjectCharter.JPG)

## 2. Requirements 
 
## 2.1. Functional Requirements

* a1) Fun: Clever Birds is fun and simple. By clicking the button "play now" on the top right or every screen, the user can start playing the game. 
* a2) User Profile: After registration, all users have their personal profile.
* a3)  Suitable for kids 5-8 years old: Clever Birds is very simple. After signing in, the user can see a green button on the top right ("PLAY NOW!") on all screens. By pressing the button, the user starts playing.  
* a4) Unique selling point: A chatbot to talk to parents about the skills their children can gain.  
* a5) Player persona: The application allows users to choose between three avatars.
* a6) Cancelation of subscription:  On the page "Manage Account", users can delete their account, which will erase their data from our database. 
* a7) Safety: The chatbot "Tweety" teaches parents how to protect their children by discussing video games' health problems and how to solve them.


## 2.2. Non-functional Requirements

* b1) The UI should be usable with 1 hand: In the Clever Birds game, the player pilots the bird into the pipes, by clicking with the mouse.
* b2) Data must be stored in the most efficient way: Our application stores data efficiently, as explained in Appendix X: “Database Design”. 
* b3) Data must be able to be searched and managed as efficiently as possible: In our application data can be managed efficiently, as explained in Appendix X: “Database Design.

## 2.3. High priority requirements

From the agreed ten requirements received, we have chosen five as high priority due to their importance to the overall product functionality and design:

* a2) 	User profiles play a vital role in user experience as it provides a collection of information associated with users. 
* a3) 	The game should be easy to understand and the user’s path to playing the game very simple. 
* a5) One of the key features of what sets Clever Birds aside from Flappy Birds, is the ability for a user to choose an avatar. 
* a6) In order to comply with the GDPR, we allow users to delete their account at any time and their data will be deleted from our database.
* a7) Another key feature setting the application apart from Flappy Birds is a safety feature informing parents about health problems related to video games. 

## 3. How to use our platform

Here is a summary showing how to use our platform step-by-step:
 
>  * STEP 1 - USER NAVIGATION: Users can navigate the platform and use the chatbot "Tweety", even if they are not registered. 
>  * STEP 2 - REGISTRATION: For user registration there are four parameters: first name, username, email and password.  
>  * STEP 3 - LOGIN: For user login there are two parameters: username and password.  
>  * STEP 4 - GDPR: Registered users are able to see his or her stored personal details and delete it from our database (for GDPR compliance)  
>  * STEP 5 - TWEETY: Registered and Unregistered users are able to talk to our chatbot "Tweety".  
>  * STEP 5 - GAME: Registered users are able to play Clever Birds.  

## 4. Clever Birds Game 

 ![play](https://cdn.discordapp.com/attachments/951482776895508504/972851900963770398/Screen-Recording-2022-05-08-at-1_1.gif)


## 5. Project Architecture 

This project uses the Model-View-Controller (MVC) architecture framework, which can be described as an architectural pattern that separates an application
into three main logical components: model (data), view (user interface), and controller (processes that handle input). Here is our architeture:

* Model => The type of data we are using in the application: user's data 
* View => Our interfaces (Html/CSS/Javascript)  
* Controller => In the file with x controllers:  

> :radio_button: We have eight routes, with the following features: 
> * :arrow_forward: 1 - user registration (users can registrate by providing name, username, email and password) 
> * :arrow_forward: 2 - user login (users can registrate by providing username and password) 
> * :arrow_forward: 3 - game (users can play Clever Birds) 
> * :arrow_forward: 4 - change avatar (will allow users to change the avatar)
> * :arrow_forward: 5 - manage account (will allow users to see in their profile their information and allow them to delete their account and data from our database)
> * :arrow_forward: 6 - talk to tweety (will allow users to speak to our chatbot "Tweety")
> * :arrow_forward: 7 - about (will inform how to use the platform) 
> * :arrow_forward: 8 - privacy policy (will inform users of the personal data we collect when they access/use the Website and how we protect their personal data)


## 5.1. Activity Diagram

Click the links below to see the activity diagram:

* [Clever Birds - Activity Diagram](https://github.com/SEPM-2022/CleverBirds/blob/develop/assets/March-16ActivityDiagram-CleverBirds-Website.jpg) 


## 5.2 Project Structure

The following directory diagram was generated with the following command in the terminal: "tree /F"
 

```
C:.
│   .gitignore
│   app.py
│   app.sqlite
│   Dockerfile
│   privacy-policy-page.html
│   README.md
│   requirements.txt
│   start.sh
│   test-e2e.sh
│   test.sh
│   tests.py
├───assets
│       CleverBirdsDB.sql
│       March-14-ActivityDiagram-CleverBirds-Website.drawio.pdf
│       March-16ActivityDiagram-CleverBirds-Website.jpg
│       simpledb-april.JPG
├───controllers
│   │   chatbot.py
│   │   game_controller.py
│   │   users_controller.py
│   │   user_documentation.py
│   └───__pycache__
│           chatbot.cpython-38.pyc
│           game_controller.cpython-38.pyc
│           users_controller.cpython-38.pyc
│           user_documentation.cpython-38.pyc
├───e2e
│   │   cypress.json
│   │   package-lock.json
│   │   package.json
│   └───cypress
│       └───integration
│               dynamic-pages.spec.js
│               static-pages.spec.js
├───models
│   │   clever_users.py
│   │   game_instance.py
│   │   music.py
│   └───__pycache__
│           clever_users.cpython-38.pyc
│           game_instance.cpython-38.pyc
│           music.cpython-38.pyc
├───static
│   │   dashboard.css
│   │   index.css
│   ├───img
│   └───js
│       └───game
│           │   .browserslistrc
│           │   .eslintrc.json
│           │   .gitignore
│           │   angular.json
│           │   jest-global-mocks.ts
│           │   jest.config.js
│           │   package-lock.json
│           │   package.json
│           │   README.md
│           │   setup-jest.ts
│           │   tsconfig.app.json
│           │   tsconfig.json
│           │   tsconfig.spec.json
│           │   tslint.json
│           │
│           ├───dockerfiles
│           │       build.Dockerfile
│           │       test.Dockerfile
│           ├───e2e
│           │   │   protractor.conf.js
│           │   │   tsconfig.json
│           │   │
│           │   └───src
│           │           app.e2e-spec.ts
│           │           app.po.ts
│           └───src
│               │   favicon.ico
│               │   index.html
│               │   main.ts
│               │   polyfills.ts
│               │   styles.scss
│               ├───app
│               │   │   app-routing.module.ts
│               │   │   app.component.html
│               │   │   app.component.scss
│               │   │   app.component.spec.ts
│               │   │   app.component.ts
│               │   │   app.module.ts
│               │   │   window.token.ts
│               │   └───components
│               │       └───game-over
│               │               game-over.component.html
│               │               game-over.component.ts
│               ├───assets
│               │   │   .gitkeep
│               │   └───img
│               └───environments
│                       environment.prod.ts
│                       environment.ts
├───templates
│       about.html
│       au.html
│       change-avatar.html
│       choose-avatar.html
│       create-account.html
│       footer.html
│       head.html
│       header.html
│       index.html
│       manage-account.html
│       playgame.html
│       privacy-policy.html
│       signup-success.html
│       tweety.html
│       user-dashboard.html
└───__pycache__
        app.cpython-38.pyc
```

## 8. Python Dependencies

* [**flask**](http://flask.pocoo.org/) 
* [**Werkzeug**](https://pypi.org/project/Werkzeug/) - for password hashing RESTful API documentation.
* [**Pyodbc**](https://pypi.org/project/pyodbc/) - for accessing the database and carry out user registration.
* [**Requests**](https://pypi.org/project/requests/) - for making HTTP requests in Python. 
 
 
## 9. Tools

* [**Docker**](https://www.docker.com/) - for storing the database and the API in a container. 
* [**Ngrok**](https://ngrok.com/) - enabled the exposure of the a local development server to the Internet with minimal effort. 
* [**Github**](https://github.com/alicevillar/sfa_api) - to store the code and document the project. 
* [**Insomnia**](https://insomnia.rest/) - used to consume APOD and retrieve the 365 images for our dataset (monolithic architecture). 
* [**JIRA**](https://www.atlassian.com/software/jira?&aceid=&adposition=&adgroup=89541890822&campaign=9124878120&creative=542569520122&device=c&keyword=jira%20project%20management%20software&matchtype=e&network=g&placement=&ds_kids=p51241495749&ds_e=GOOGLE&ds_eid=700000001558501&ds_e1=GOOGLE&gclid=CjwKCAjw9LSSBhBsEiwAKtf0n46U4jUddN6hDaMFm69grPXSOFett05-wHANMVWGpSxsxZ8G_RdhwxoC6moQAvD_BwE&gclsrc=aw.ds) - used for project management. 
* [**CONFLUENCE**](https://www.atlassian.com/software/confluence?&aceid=&adposition=&adgroup=96330466462&campaign=9612124506&creative=425915242014&device=c&keyword=%2Bconfluence&matchtype=b&network=g&placement=&ds_kids=p52353042127&ds_e=GOOGLE&ds_eid=700000001542923&ds_e1=GOOGLE&gclid=Cj0KCQjw1ZeUBhDyARIsAOzAqQI6_HrbY2AqRc9qHw7d-FEv1V8S5twWSk_v-Y53l-PRSiQIt9BVRvkaAljLEALw_wcB&gclsrc=aw.ds) - for documentation.
* [**Dbeaver**](https://dbeaver.pro/?url=https://dbeaver.io/
) - we used as an interface for our database (SQLite). Allowed us to document our tests in our database. 
* [**SourceTree**](https://www.sourcetreeapp.com/)) - to better vizualize our work as a team using gitflow.  

 
## 10. Installation

### Using python
We suggest to setup a virtual environment first.

```
$ pip install -r requirements.txt

$ flask run
```
 
### Using docker

```
$ docker build -t clever-bird .

$ docker run -d -p 5000:5000 clever-bird
``` 
 
## 11. Confluence documentation 

Throughout the development of this project, we used Confluence to develop our product documentation, track meeting minutes, draw process flow diagrams, and create technical architecture documents. Please click here to access our [Confluence Documentation - PDF](https://github.com/SEPM-2022/CleverBirds/blob/develop/assets/CONFLUENCE-PDF-NEW.pdf)

:arrow_forward: In the Confluence Documentation PDF is not possible to visualize the Gantt Chart, Raci Matrix and Test Report, so we have included these items here:

* [Gantt Chart](https://github.com/SEPM-2022/CleverBirds/blob/develop/assets/GanttChart%20CB.pdf)
* [RACI Matrix](https://github.com/SEPM-2022/CleverBirds/blob/develop/assets/RACI-MATRIX-CB.pdf)
* [Test Report](https://github.com/SEPM-2022/CleverBirds/blob/develop/assets/Test%20Report.pdf)
 

 ## 12. Useful Links  
 
[Flask Quickstart](https://flask.palletsprojects.com/en/2.0.x/quickstart/)
 
[SQL Alchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/#a-minimal-application) 
 
[GITHUB project guidelines](https://gist.github.com/rsp/057481db4dbd999bb7077f211f53f212)

[GIT FLOW](http://danielkummer.github.io/git-flow-cheatsheet/)

[GIT FLOW Atlassian](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)

[CLIPART MAX](https://www.clipartmax.com)

[CLIPART LIBRARY](http://clipart-library.com/)


 

  
