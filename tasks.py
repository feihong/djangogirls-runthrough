"""
This file contains some shortcuts for running programs on the command line.

"""
import subprocess
from invoke import task


@task
def serve(ctx):
    subprocess.call('python manage.py runserver', shell=True)


@task
def shell(ctx):
    subprocess.call('python manage.py shell', shell=True)
