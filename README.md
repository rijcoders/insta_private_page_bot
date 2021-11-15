# python bot

## Requirments

- selenium
- chromdriver
- requests
- os
- urllib

## initial setup

create virtual env

- windows
```bash
python -m venv env
```
- Linux/MacOs
```bash
python3 -m pip install --user virtualenv
```

## How to use code

- You should enter your username in inital class and your password in secret.py (You can also create virtaul variable for more safty)
- After you add your username and password you can login in to your account two ways my suggest is to use "login_by_xpath()"
- When login function fully excuted it goes to "go_to_page" function and it will go directly to video section of that page tou should inital "You wanted page" 
- then in for loop you should specify how many videos do you want to download


## Run
For running project just type 
```bash 
python bot.py
```
