"""
This file contains some shortcuts for running programs on the command line.

"""
from invoke import task


@task
def serve(ctx):
    ctx.run('python manage.py runserver')
