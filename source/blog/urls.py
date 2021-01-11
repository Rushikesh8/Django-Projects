"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include
from django.contrib import admin
from django.urls import path

from posts.views import blog
from posts.views import post
from posts.views import search
from posts.views import post_create
from posts.views import post_update
from posts.views import post_delete
from posts.views import about_us


urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include ('tinymce.urls')),
    path('', blog, name='post_list'),
    path('search/', search, name= 'search'),
    path('create/', post_create, name='post_create'),
    path('post/<id>/',post, name= 'post_detail'),
    path('post/<id>/update/',post_update, name='post_update'),
    path('post/<id>/delete/',post_delete, name='post_delete'),
    path('accounts/', include('allauth.urls')),
    path('about/',about_us,name='about_us')
    

] + static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)
