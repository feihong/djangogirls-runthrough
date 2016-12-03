from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('^login/$', auth_views.login, name='login'),
    url('^logout/$', auth_views.logout, name='logout'),
    url(r'', include('blog.urls')),
]
