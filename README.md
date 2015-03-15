ZUKS-Controller
===============
![Travis build status](https://travis-ci.org/ZUKSev/ZUKS-Controller.svg?branch=master)

Web application for the organisation of volunteers in Civil Support.
![Controller Sreenshot](https://raw.githubusercontent.com/ZUKSev/ZUKS-Controller/master/Images/controller-screenshot-01.png)

## Installation
- Switch to new a python 2.x or 3.x environment with `virtualenv` _(optional)_
- Install python dependencies `pip install -r requirements.txt`

### Websocket Server
- `cd websocket-server`
- Configure the server port in the `settings.py` file
- Start server `python server.py`

### REST-Server
- `cd server`
- Configure server `server/settings.py`. Most important settings:
	- `SECRET_KEY` (the existing one should be only used for debug purposes)
	- `DEBUG`
	- `TEMPLATE_DEBUG`
	- `CORS` (Important, when the client files are not served under the same URL as the REST-Server. [Read more.](https://github.com/ottoyiu/django-cors-headers#configuration))
	- `WEB_SOCKET_SERVICE_URL` (as configured above))
- Create database `python manage.py migrate`
- Load fixtures `python manage.py loaddata POICategories`
- Start server `python manage.py runserver #ip#:#port#` or embedded via wsgi

### Web-Server
- `cd client`
- Install node dependencies `npm install` (Dependency: [node.js](https://nodejs.org/))
- Install grunt `npm install -g grunt-cli` ([Read more](http://gruntjs.com/getting-started))
- Deploy Webserver `grunt install`
- Serve one of the following static files (For example by `python -m SimpleHTTPServer #web-port#`)
	-  `dist/controller/index.html`, 
	- `dist/client/index.html` or 
	- `dist/demo/index.html`
