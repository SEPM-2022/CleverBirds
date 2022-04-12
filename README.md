 <h1>Clever Birds: Embracing Your Children’s Passion for Video Games </h1>
 
Clever Birds is a game based on the Flappy Bird game. The difference is that in Clever Birds the user is able to choose three avatars: Daisy, Alfredo and Birdy and be provided informative information by means of a chatbot. The gameplay requires the player to navigate the little bird through gaps between the pipes without hitting them, continuously earning a point as he/she passes through each pipe.

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
- [3. Clever Birds Webpage](#3-clever-birds-webpage)
    - [3.1. How to use our platform](#31-how-to-use-our-platform)
    - [3.2. Activity Diagram](#32-activity-diagram)
- [4. Clever Birds Game](#3-clever-birds-game)
    - [4.1. Game Play](#31-game-play)
    - [4.2. Game Activity Diagram](#32-game-activity-diagram) 
- [5. Project Architecture](#3-project-architecture)
- [6. Project Structure](#5-project-structure)
- [7. Project Files](#6-project-files)
- [8. Python Dependencies](#7-python-dependencies) 
- [9. Tools](#8-tools) 
- [10. Installation](#9-installation)
- [11. Demo](#10-demo)
- [12. Testing](#13-automated-testing)
- [13. Project Roadmap](#14-project-roadmap)
- [14. Useful Links](#15-useful-links)


 

<!-- /TOC -->
 
## 1. Overview 

This API, called SFA (Space Fan Art), is an API created with Flask REST-Plus with two Prototypes: a monolithic architecture and a microservice architecture. [Astronomy Picture Of The Day (APOD)](https://api.nasa.gov/), which is a NASA open API that returns the picture of the day, has been used as a model thoughout the development of both Prototypes:  
 
:arrow_forward: In the monolithic architecture, APOD was used as an API model in various aspects, such as user authorisation key and rate limits. 
<br>
:arrow_forward:In the microservice architecture, SFA-API is connected with APOD. Thus, our microservive returns a picture that comes directly from APOD. 

<br> 
 
## 2. Requirements 

 
## 2.1. Functional Requirements

* a1) Adam is a four-year-old boy. He wants the game to be fun: In the Clever Birds is based on the classical Flappy Bird game, which has proven to be very easy and fun. Clever Birds also allows the player to choose other avatars, which will make the game more engaging and personal. 

* a2) A player should be able to create a user profile: as shown in Appendix 3, the system will allow the player to create a user profile. 

* a3) Jenna is a five-year-old girl. She doesn’t want to have to ask mum for help: as shown in Appendix X, after registration, it is very simple to sign in and by pressing a button on the top right of the screen (“PLAY NOW”) the user starts playing. 

* a4) Andrew works in a toy shop. He wants the game to have a unique selling point: The unique selling point of the game is the fact that it has a chatbot to talk to parents about the skills their children can gain.  

* a5) A player should be able to create a persona: As it is shown in Appendix X (“Choose your avatar”), the application allows users to choose one of the following avatars: Daisy, Alfredo and Birdy. 

* a6) A customer can cancel their subscription at any time: As it is shown in Appendix X, in the “User Dashboard”, users can delete their account at any time and their data will be deleted from our database. 

* a7) Kashif is a 30 year old dad. He wants the game to be safe: Some of the main dangers of video games are cyber bullying, privacy problems, personal information on consoles, computers and devices, webcam worries, online predators, hidden Fees and Malware (Kapersky, 2022) This project introduces a chatbot named “Tweety”. It will be able to explain to parents how to protect their children and enhance the gaming experience by discussing health problems related to video-games and how to solve them.


## 2.2. Non-functional Requirements

> :small_orange_diamond: Design based on a microservice architecture, using MVC (Model-View-Controller) pattern.  


* b1) The UI should be usable with 1 hand: In the Clever Birds game, the player pilots the bird into the pipes, by clicking with the mouse.

* b2) Data must be stored in the most efficient way: Our application stores data efficiently, as explained in Appendix X: “Database Design”. 

* b3) Data must be able to be searched and managed as efficiently as possible: In our application data can be managed efficiently, as explained in Appendix X: “Database Design.
 
## 3. Clever Birds Webpage 

This project uses the Model-View-Controller (MVC) architecture framework, which can be described as an architectural pattern that separates an application
into three main logical components: model (data), view (user interface), and controller (processes that handle input). Here is our architeture:

* Model => The type of data we are using in the application: user's data 
* View => Our interfaces (Html/CSS/Javascript)  
* Controller => In the file with x controllers:  

> :radio_button: We have eight routes, with the following features: 
>  :arrow_forward: 1 - user registration (users can registrate by providing name, username, email and password) 
>  :arrow_forward: 2 - user login (users can registrate by providing username and password) 
>  :arrow_forward: 3 - game (users can play Clever Birds) 
>  :arrow_forward: 4 - change avatar (will allow users to change the avatar)
>  :arrow_forward: 5 - manage account (will allow users to see in their profile their information and allow them to delete their account and data from our database)
>  :arrow_forward: 6 - talk to tweety (will allow users to speak to our chatbot "Tweety")
>  :arrow_forward: 7 - about (will inform how to use the platform) 
>  :arrow_forward: 8 - privacy policy (will inform users of the personal data we collect when they access/use the Website and how we protect their personal data)


![print](/readme_img/swagger_print.PNG)  
 

## 3.1. How to use our platform

Here is a summary showing how to use our platform step-by-step:
 
>  * STEP 1 - USER NAVIGATION: Users can navigate the platform and use the chatbot "Tweety", even if they are not registered. 
>  * STEP 2 - REGISTRATION: For user registration there are four parameters: first name, username, email and password.  
>  * STEP 3 - LOGIN: For user login there are two parameters: username and password.  
>  * STEP 4 - GDPR: Registered users are able to see his or her stored personal details and delete it from our database (for GDPR compliance)  
>  * STEP 5 - TWEETY: Registered and Unregistered users are able to talk to our chatbot "Tweety".  
>  * STEP 5 - GAME: Registered users are able to play Clever Birds.  


## 3.2. Activity Diagram

Click the links below to see the activity diagram:

* [Clever Birds - Activity Diagram](link) 


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
 

## 6. Project Structure

The following directory diagram was generated with the following command in the terminal: "tree /F"
 

## 7. Project Files

* `README.md` [README.md](https://github.com/SEPM-2022/CleverBirds/blob/develop/README.md)- Contains the description and documentation of the project. 
* `app.py` [app.py](https://github.com/SEPM-2022/CleverBirds/blob/develop/app.py) - Creates the database and defines all the routes.   
* `Dockerfile`[Dockerfile](https://github.com/SEPM-2022/CleverBirds/blob/develop/Dockerfile) - Docker config file to build a Docker image.
* `common_passwords.py` [common_passwords.py](https://github.com/alicevillar/sfa_api/blob/main/useful/common_passwords) - File containing the 1000 most common passwords. 
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
 
 
<h3>Using Docker</h3>

It's easy to start exploring our platform using Docker:
 
  
## 11. Quick Start  
 
 <br>
 Check our web application with the following link:  
 <br>

## 12. OWASP Proactive Controls

The [OWASP Top Ten Proactive Controls](https://owasp.org/www-project-proactive-controls/) is a list of security techniques that should be included in every software development project. They are ordered by order of importance, with control number 1 being the most important. 

 <h3>C1: Define Security Requirements</h3>

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

<h3>C4: Encode and Escape Data</h3>

Encoding and escaping are defensive techniques meant to stop injection attacks. Here is the OWASP definition:
 * Encoding (commonly called “Output Encoding”) involves translating special characters into some different but equivalent form that is no longer dangerous in the target interpreter, for example translating the < character into the &lt; string when writing to an HTML page. 
 * Escaping involves adding a special character before the character/string to avoid it being misinterpreted, for example, adding a \ character before a " (double quote) character so that it is interpreted as text and not as closing a string.
 
> :white_check_mark: We don't apply encoding or escaping because it was not needed. 
> 
> :o: It should be highlightened that a hash is not ‘encryption’ – it cannot be decrypted back to the original text (it is a ‘one-way’ cryptographic function, Whereas
> encryption is a two-way function, hashing is a one-way function. Hashing is used in conjunction with authentication to produce strong evidence that a given message has not
> been modified and serves the purpose of ensuring integrity, i.e. making it so that if something is changed you can know that it’s changed password is stored in hashed into
> the database and the authentication process uses hashing comparison. For password hashing we use the library [Werkzeug](https://pypi.org/project/Werkzeug/). 

<h3>C5: Validate All Inputs</h3>

Input validation is a programming technique that ensures only properly formatted data may enter a software system component. It validates that an input value is what you think it should be. Syntax validity means that the data is in the form that is expected. 

> :white_check_mark: To validate inputs we use the Python library [Validator Collection](https://pypi.org/project/validator-collection/), which is a Python library that provides functions that can be used to validate the type and contents of an input value.  
 
 

 <h3>C7: User Experience Monitoring</h3>
 
 > :white_check_mark: In Clever Birds, we monitor the user experience through our chatbot Tweety, who asks questions to users about their experience. 

 
<h3>C8: Protect Data Everywhere</h3>
 

> :white_check_mark: In Clever Birds, we protect data with parametrised queries to protect against SQL injection. OWASP recommends stored procedures but this is not done here because the queries are small, so this measure is unecessary. OWASP also recommends escaping, which we didn't need to do in our project because it wasn't necessary.
 
<h3>C9: Implement Security </h3>
  
Here is how we will implement secure user authentication system using the Python library [Werkzeug](https://werkzeug.palletsprojects.com/en/2.0.x/utils/):

> :white_check_mark:We won’t store passwords in plaintext in the database, but instead encrypt passwords using hashes.
> :white_check_mark:Passwords stored as hash are irreversible to plaintext (one way hash).
> :white_check_mark:With a given hash, attackers cannot guess the plaintext.  
 

<h3>C10:  Handle All Errors and Exceptions</h3>  

Exception handling is a programming concept that allows an application to respond to different error states (like network down, or database connection failed, etc) in various ways. Handling exceptions and errors correctly is critical to making your code reliable and secure. The try block lets you test a block of code for errors. The except block lets you handle the error.  

## 13. Testing

 
<h3>Here is our testing plan:</h3>  
 
 

## 14. Project Roadmap 

To take this project further: 

* WEB INTERFACE: Improve....
* AWS: Host the project in AWS, which offers reliable, scalable, and inexpensive cloud computing services.

 
 ## 15. Useful Links  
 
 
 [Flask Quickstart](https://flask.palletsprojects.com/en/2.0.x/quickstart/)
 
 [SQL Alchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/#a-minimal-application) 
 
 [GITHUB project guidelines](https://gist.github.com/rsp/057481db4dbd999bb7077f211f53f212)
 
 [Flask Testing](]https://pythonhosted.org/Flask-Testing/)
 
[GIT FLOW](http://danielkummer.github.io/git-flow-cheatsheet/)

[GIT FLOW Atlassian](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)


  
