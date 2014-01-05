mySociety questionnaire
===

This is an assignment from mySociety to create:

> a demo web application that could be used alongside a live-streamed election broadcast, to provide an unscientific straw-poll of the voting habits of the viewers. 

I'm creating this in [Django](https://www.djangoproject.com/), and I'll host a demo of the application on [Heroku](https://www.heroku.com/).

Running locally
---

Here are the steps to getting this running locally. You don't have to follow this exactly, if you'd like to use [virtualenv](https://pypi.python.org/pypi/virtualenv) or something, but outlined below is the simplest approach, assuming you're on a Debian-based system.

After cloning the project, run the following from inside it:

``` bash
$ sudo apt-get install python-pip      # Install pip
$ sudo pip install -r requirements.txt # Install python dependencies
$ ./manage syncdb
$ ./manage runserver
```

Now browse to <127.0.0.1:8000>.
