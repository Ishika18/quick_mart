# QUICK MART

## Setup

1. Clone the repository:

```sh
$ git clone https://github.com/Ishika18/quick_mart.git
$ cd quick_mart
```

2. Create a virtual environment:

```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```

3. Installing and activating dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

4. Add an environment variable with key "SECRET_KEY" and value with a generated secret key or change SECRET_KEY = os.environ.get('SECRET_KEY') to a string representing secret key(settings.py line 14). Former is preffered.

5. Once `pip` has finished downloading the dependencies and secret key is added:
```sh
(env)$ cd project
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.


## Walkthrough

1. Log In / Register.
2. Pick and update food preference ( click Preferences in navbar ).
3. Click the scan button and scan barcode of the food item.

## Features and description
1. User authentication
2. Text search suggestions using algolia
3. Profile update
4. Scanner
5. Food database result using Spoonacular API.

## Technologies used
1. Python/ Django
2. SQLlite3
3. Pyzbar
4. HTML
5. CSS
6. JavaScript
7. [Algolia API](https://www.algolia.com/)
8. [Spoonaculat API](https://spoonacular.com/food-api)

