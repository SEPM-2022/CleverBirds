 <h1>Clever Birds: Embracing Your Children’s Passion for Video Games </h1>
 
This presentation is focused on the project management process of building our platform, a Javascript integration of game via API. “Clever Birds”, a game in which the player navigates the avatar bird through obstacles without hitting them, earning points as he or she passes each pipe. The application has a chatbot named “Tweety”, who guides parents about how to use their children's game time as an educational experience. 

:arrow_forward: Duration : 3 months
<br>
:arrow_forward: Team : Teamwork of 4

<h3>Currently in progress ! 💻</h3>

> :round_pushpin: Goals to be achieved: 
> * A light-weight demonstration of a working model of the web application Clever Birds and the description of testing. 
 
 <h1>Table of Contents</h1>

<!-- TOC -->
- [1. Overview](#1-overview)
- [2. Requirements](#2-requirements) 
    - [2.1. Functional Requirements](#21-functional-requirements)
    - [2.2. Non-functional Requirements](#22-non-functional-requirements)
- [3. How to use our platform](#3-how-to-use-our-platform)
- [4. Clever Birds Game](#4-clever-birds-game)
    - [4.1. Game Play](#41-game-play)
    - [4.2. Game Activity Diagram](#42-game-activity-diagram) 
- [5. Project Architecture](#5-project-architecture)
   - [5.1. Activity Diagram](#51-activity-diagram)
- [6. Project Structure](#6-project-structure)
- [7. Project Files](#7-project-files)
- [8. Python Dependencies](#8-python-dependencies) 
- [9. Tools](#9-tools) 
- [10. Installation](#10-installation)
- [11. Demo](#11-demo)
- [12. Testing](#12-automated-testing)
- [13. Project Roadmap](#13-project-roadmap)
- [14. Confluence Documentation](#13-confluence-documentation)
- [15. Useful Links](#15-useful-links)


 

<!-- /TOC -->
 
## 1. Overview 

This API, called SFA (Space Fan Art), is an API created with Flask REST-Plus with two Prototypes: a monolithic architecture and a microservice architecture. [Astronomy Picture Of The Day (APOD)](https://api.nasa.gov/), which is a NASA open API that returns the picture of the day, has been used as a model thoughout the development of both Prototypes:  
 
:arrow_forward: In the monolithic architecture, APOD was used as an API model in various aspects, such as user authorisation key and rate limits. 
<br>
:arrow_forward:In the microservice architecture, SFA-API is connected with APOD. Thus, our microservive returns a picture that comes directly from APOD. 

<br> 
 
## 2. Requirements 

 
## 2.1. Functional Requirements

* a1) Fun: Clever Birds is fun and simple. According to Rosewater (2011), the real way to determine if a game is fun is to ask the players if they would play again. We will do this through our chatbot Tweety in a customer satisfaction survey. 
* a2) User Profile: Users can create a user profile.
* a3)  Suitable for kids 5-8 years old: Clever Birds is very simple. After signing in, the user can see a green button on the top right ("PLAY NOW!") on all screens. By pressing the button, the user starts playing.  
* a4) Unique selling point: A chatbot to talk to parents about the skills their children can gain.  
* a5) Player persona: The application allows users to choose between three avatars.
* a6) Cancelation of subscription:  On the page "Manage Account", users can delete their account, which will erase their data from our database. 
* a7) Safety: The chatbot "Tweety" teaches parents how to protect their children by discussing video games' health problems and how to solve them.


## 2.2. Non-functional Requirements

> :small_orange_diamond: Design based on a microservice architecture, using MVC (Model-View-Controller) pattern.  

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

![print](/readme_img/swagger_print.PNG)  
 
## 4.1. Game Play

xxxxx

## 4.2. Game Activity Diagram


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


## 6. Project Structure

The following directory diagram was generated with the following command in the terminal: "tree /F"
 

## 7. Project Files

* `README.md` [README.md](https://github.com/SEPM-2022/CleverBirds/blob/develop/README.md)- Contains the description and documentation of the project. 
* `app.py` [app.py](https://github.com/SEPM-2022/CleverBirds/blob/develop/app.py) - Creates the database and defines all the routes.   
* `Dockerfile`[Dockerfile](https://github.com/SEPM-2022/CleverBirds/blob/develop/Dockerfile) - Docker config file to build a Docker image.
* `application_structure.py` [application_structure.py](https://github.com/alicevillar/sfa_api/blob/main/application_structure.py) - Directory tree structure in Python.
* `requirements.txt` [requirements.txt](https://github.com/SEPM-2022/CleverBirds/blob/develop/requirements.txt) - The list of Python (PyPi) requirements. Script: 1) pip install pipreqs; 2) pipreqs --encoding=utf8 C:\Users\Alice\PycharmProjects\SFA_DB 


## 8. Python Dependencies

  [*flask*](http://flask.pocoo.org/))  
* [**Werkzeug**](https://pypi.org/project/Werkzeug/) - for password hashing RESTful API documentation.
* [**Pyodbc**](https://pypi.org/project/pyodbc/) - for accessing the database and carry out user registration.
* [**Requests**](https://pypi.org/project/requests/) - for making HTTP requests in Python. 
* [**Validator Collection**](https://pypi.org/project/validator-collection/) - to validade users' inputs. 
* [**Dependency Check**](https://pypi.org/project/dependency-check/) - scans application dependencies and checks whether they contain any published vulnerabilities.

 
## 9. Tools

* [**Docker**](https://www.docker.com/) - for storing the database and the API in a container. 
* [**Ngrok**](https://ngrok.com/) - enabled the exposure of the a local development server to the Internet with minimal effort. 
* [**Github**](https://github.com/alicevillar/sfa_api) - to document the project. 
* [**Insomnia**](https://insomnia.rest/) - used to consume APOD and retrieve the 365 images for our dataset (monolithic architecture). 
* [**JIRA**](https://www.atlassian.com/software/jira?&aceid=&adposition=&adgroup=89541890822&campaign=9124878120&creative=542569520122&device=c&keyword=jira%20project%20management%20software&matchtype=e&network=g&placement=&ds_kids=p51241495749&ds_e=GOOGLE&ds_eid=700000001558501&ds_e1=GOOGLE&gclid=CjwKCAjw9LSSBhBsEiwAKtf0n46U4jUddN6hDaMFm69grPXSOFett05-wHANMVWGpSxsxZ8G_RdhwxoC6moQAvD_BwE&gclsrc=aw.ds) - used for project management. 


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
 
  
## 11. Quick Start  
 
 <br>
 Check our web application with the following link:  
 <br>

## 12. Security Controls

The [OWASP Application Security Verification Standard (ASVS)](https://owasp.org/www-project-application-security-verification-standard/) contains categories such as authentication, access control, error handling / logging, and web services. Each category contains a collection of requirements that represent the best practices for that category drafted as verifiable statements.  

>  :white_check_mark: Security requirements: 
>  * Protect against injection: We use parameterised queries to avoid SQL injection attacks in all the operations with the database. 
>  * Protect  Data: protected password with hashing.  
>  * Broken Access Control: Restrictions on what users are allowed to do. 
>  * Protect against Cross-Site Scripting (XSS): We protect against XSS in our web page, using javascript. 
   
 <h3>C2: Leverage Security Frameworks and Libraries</h3>

Secure frameworks and libraries can help to prevent a wide range of web application vulnerabilities.  

>  :white_check_mark: In Clever Birds we do a [dependency check](https://securityguide.github.io/webapps/tools/python-tools/python-dependency-checker.html) to detect publicly disclosed vulnerabilities contained within a project's dependencies. Click [here](https://github.com/alicevillar/sfa_api/blob/main/readme_img/dependency_check.JPG) to see the result.  

 <h3>C3: Secure Database Access</h3>

 According to OWASP, secure access to databases consider: secure queries, secure configuration, secure communication and secure authentication. 

>  :white_check_mark: Clever Birds handles secure database access with the following measures: 
> * Secure queries: In order to mitigate SQL injection we used ‘Query Parameterization’. However, certain locations in a database query are not parameterisable. Because of the large variation in the pattern of SQL injection attacks they are often unable to protect databases. OWASP recommends testing queries for performance, but this is not done here because the queries are all very small and therefore it is not necessary. 
> * Secure configuration: we run the database in a docker container, which has connectivity restrictions (can only be accessed by the administrator and only has one door open - 1433). The server which runs the database does not allow external access. All access to the database should be properly authenticated. Thus, it is not possible to directly access the database from outside the instance. 
> * Secure communication: we use Pyodbc, an open source Python module to communicate with the database. We apply secure (authenticated, encrypted) communications methods.  

 <h3>C7: User Experience Monitoring</h3>
 
 > :white_check_mark: In Clever Birds, we monitor the user experience through our chatbot Tweety, who asks questions to users about their experience. 

<h3>C8: Protect Data Everywhere</h3>
 
> :white_check_mark: In Clever Birds, we protect data with parametrised queries to protect against SQL injection. OWASP recommends stored procedures but this is not done here because the queries are small, so this measure is unecessary. OWASP also recommends escaping, which we didn't need to do in our project because it wasn't necessary.
 
<h3>C9: Implement Security </h3>
  
Here is how we will implement secure user authentication system using the Python library [Werkzeug](https://werkzeug.palletsprojects.com/en/2.0.x/utils/):

> :white_check_mark:We won’t store passwords in plaintext in the database, but instead encrypt passwords using hashes.
> :white_check_mark:Passwords stored as hash are irreversible to plaintext (one way hash).
> :white_check_mark:With a given hash, attackers cannot guess the plaintext.  

## 13. Testing
 
<h3>Here is our testing plan:</h3>  
 
 
## 14. Confluence documentation 

Throughout the development of this project, we used Confluence to develop our product documentation, track meeting minutes, draw process flow diagrams, and create technical architecture documents. Please click here to access the Confluence Documentation file: XXXXXXXXXXxx

## 15. Project Roadmap 

To take this project further: 

* WEB INTERFACE: Improve....
* AWS: Host the project in AWS, which offers reliable, scalable, and inexpensive cloud computing services.

 
 ## 16. Useful Links  
 
 
 [Flask Quickstart](https://flask.palletsprojects.com/en/2.0.x/quickstart/)
 
 [SQL Alchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/#a-minimal-application) 
 
 [GITHUB project guidelines](https://gist.github.com/rsp/057481db4dbd999bb7077f211f53f212)
 
 [Flask Testing](]https://pythonhosted.org/Flask-Testing/)
 
[GIT FLOW](http://danielkummer.github.io/git-flow-cheatsheet/)

[GIT FLOW Atlassian](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)


  
