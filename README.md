mySociety questionnaire
===

This is an assignment from mySociety to create:

> a demo web application that could be used alongside a live-streamed election broadcast, to provide an unscientific straw-poll of the voting habits of the viewers. 

I'm creating this in [Django](https://www.djangoproject.com/), and I'll host a demo of the application on [Heroku](https://www.heroku.com/).

Demo application on Heroku
---

<http://mysociety-questionnaire.herokuapp.com/>

Running locally
---

Here are the steps to getting this running locally. You don't have to follow this exactly, if you'd like to use [virtualenv](https://pypi.python.org/pypi/virtualenv) or something, but outlined below is the simplest approach, assuming you're on a Debian-based system.

### Setup

After cloning the project, run the following from inside it:

``` bash
$ sudo apt-get install python-pip      # Install pip
$ sudo pip install -r requirements.txt # Install python dependencies
$ ./manage.py schemamigration questionnaire --auto # Setup migration
$ ./manage.py syncdb                               # Create DB tables
$ ./manage.py migrate questionnaire                # Run DB data migrations
```

### Running the server

``` bash
$ ./manage runserver # Development server
```

And browse to <127.0.0.1:8000>. Or:

``` bash
$ foreman start # The gunicorn server
```

And browse to <127.0.0.1:5000>.
