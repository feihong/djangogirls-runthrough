"""
This file contains some shortcuts for running programs on the command line.

"""
import os
import subprocess
from invoke import task
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
import django
django.setup()


@task
def serve(ctx):
    """
    Run the Django server
    """
    subprocess.call('python manage.py runserver', shell=True)


@task
def shell(ctx):
    """
    Run the Django shell
    """
    subprocess.call('python manage.py shell', shell=True)


@task
def add_posts(ctx, count):
    """
    Add some test posts to the database
    """
    from django.utils import timezone
    from blog.models import Post
    from django.contrib.auth.models import User

    user = User.objects.first()
    count = int(count)

    for i in range(1, count+1):
        print('Adding post {}'.format(i))
        Post.objects.create(
            title='Post {}'.format(i),
            author=user,
            text='This is the body of post {}'.format(i),
            published_date=timezone.now(),
        )
