# INF151_MOMENTS

## A social media application meant to capture the momments we hold dear to our hearts with groups of people

This project is a startup developed during the duration and through the course work of INF 151. A group of soon to be software engineers 
has brainstormed and dilgently developed this application using frame works as close to industry standared as possible for the short time
of 10 weeks. The applications attempts to imitate a social media application with many related and standarad app features although can be
thought of as a social media shared albumn.

* users are able to create an account, login, post an image onto their page, and create a prompt with their friends.
* Python3, kivy, kivymd, sql

## Setup
1. clone this project
   git clone https://github.com/TiagoV2/INF151_MOMENTS.git

2. kivy if not installed
pip3 install kivy

3. sqlite3 if not installed
pip3 install sqlite3

4. cd PATH2 INF151_MOMENTS
  python3 main.py

## File Structure

"""
project_root/
│
├── appImages/
│   ├── friends.png
│   ├── imageEditor.py
│   └── profile.png
│
├── pages/
│   ├── createAccountPage.kv
│   ├── home.kv
│   ├── login.kv
│   ├── postImage.kv
│   ├── settings.kv
│   └── todaysPrompt.kv
│
└── userData/
    ├── loginInfoDatabase.py
    └── user_credentials.db
"""

## Known Issues / Missing Items
1. Settings Page
2. Incomplete home page
3. Logout feature
4. Adding friends
5. Posting caputured iamges


## Tutorials and References
1. Login and Sign up Page
  <a href="https://youtu.be/5X5pK9r5fdg">KIVY/KIVYMD - Login Page, Sign up Page | Python Login Screen Tutorial by Python With Sh1de</a>
  * Used the following video to get inspiration for the login page and the create account page. Watched as a team to learn how to use the framework kivy.
  * Helped create a foundation in python with kivy and using .kv files along with a main file.
  * Coupled with documenation which was found and inspected soon after was a great reference for this project.
