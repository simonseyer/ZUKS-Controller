ZUKS-Controller
===============
![Travis build status](https://travis-ci.org/Eldorado234/ZUKS-Controller.svg?branch=master)

Web application for the organisation of volunteers in Civil Support.

## Installation (Development)
- Install `virtualenv` _(optional)_, `npm` and `git`
- Create a new Python 2.x or 3.x environment with `virtualenv venv-folder` _(optional)_
- `pip install -r requirements.txt`
- Start for each terminal in the root directory

### Terminal I

- Switch to the python environment with `source venv-folder/bin/activate` _(optional)_
- `cd server`
- `python manage.py migrate`
- `python manage.py loaddata POICategories`
- `python manage.py runserver #ip#:#port#`

### Terminal II

- Switch to the python environment with `source venv-folder/bin/activate` _(optional)_
- `cd websocket-server`
- `python server.py`

### Terminal III

- `cd client`
- `bower install` _(optional)_
- `npm install` _(optional)_
- `grunt deploy`
- `cd dist`
- `python -m SimpleHTTPServer #web-port#`

### Browser
- Open `#ip#:#web-port#/client`
- Open `#ip#:#web-port#/controller`
