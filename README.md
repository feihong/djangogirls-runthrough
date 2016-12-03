# DjangoGirls Tutorial Runthrough

This is the code I wrote as I followed the [DjangoGirls tutorial](https://tutorial.djangogirls.org/). Deployed to my [PythonAnywhere account](http://feihong.pythonanywhere.com/).

## Installation

Make sure that you have virtualenvwrapper (`pip install virtualenvwrapper`) installed.

```
mkvirtualenv -p python3 djangogirls
pip install -r requirements.txt
pip install Invoke
```

## Run server

```
inv serve
```

## Run shell

```
inv shell
```

## Quickly add some fake posts

Add 10 posts:

```
inv add_posts 10
```
