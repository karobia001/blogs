# BLOG-BUSTER
## BlogBUSTER is an app that allows a user to create blogs they like and post them .Also they  get daily motivational quotes


#### By **[Dennis karobia](https://github.com/karobia001)**

## Description
The user can register and create an account where they will have the ability to login and create new posts and post them, they can also update their posts and also delete the same post. 

## BDD

| Behavior            | Input                         | Output                        | 
| ------------------- | ----------------------------- | ----------------------------- |
| Registratin | Fill in the form in the registration page | Redirects to the login page |
| Login | Fill in the form in the create new blogs | Redirects to the home page with blog posts |
| Posting blogs | In the home page, enter your pitch in text, select a category in the drop down menu and enter| Reloads the page with the pitch as the newest pitch |
| Updating and deleting blogs | Click the update button in the profile page or the delete button | Redirects the user to the updated blog or deletes the chosen blog |


## Live link

https://blog-buster12.herokuapp.com/post/1


### Prerequsites
    - Python 3.6
    - Ubuntu software

### Clone the Repo
Run the following command on the terminal:
`https://github.com/karobia001/blogs.git`


### Create a Virtual Environment
Run the following commands in the same terminal:
`sudo apt-get install python3.6-venv`
`python3.6 -m venv virtual`
`source virtual/bin/activate`

### Install dependancies
Install dependancies that will create an environment for the app to run
`pip3 install -r requirements`

### Prepare environment variables
```bash
export DATABASE_URL='postgresql+psycopg2://username:password@localhost/blog'
export SECRET_KEY='Your secret key'
```

### Run Database Migrations
```
python manage.py db init
python manage.py db migrate -m "initial migration"
python manage.py db upgrade
```

### Running the app in development
In the same terminal type:
`python3 manage.py server`

Open the browser on `http://localhost:5000/`

## Known bugs

the pictures are failing to load we will sort the problem later

## Technologies used
    - Python 3.6
    - HTML
    - Bootstrap 
    - Heroku
    - Postgresql

## Support and contact details
##### Contact me on
email : karobiamain81@gmail.com
contact : 0704355420
slack : karobiamaina




### License
LICENSED UNDER License: MIT

Copyright (c) **DENNIS KAROBIA**