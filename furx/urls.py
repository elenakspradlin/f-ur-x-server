"""
URL configuration for furx project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf.urls import include
from rest_framework import routers
from furxapi.views import UserView, ItemView, UserItemView, BlogView, FeelingView, ToDoListView
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from furxapi.views import register_user, login_user, blog_view, feeling_view, todolist_view, user_items_view

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', UserView, 'user')
router.register(r'items', ItemView, 'item')
router.register(r'useritems', UserItemView, 'useritem')
router.register(r'blogs', BlogView, 'blog')
router.register(r'feelings', FeelingView, 'feeling')
router.register(r'lists', ToDoListView, 'list')

urlpatterns = [
    path('', include(router.urls)),
    # Requests to http://localhost:8000/register will be routed to the register_user function
    path('register', register_user),
    # Requests to http://localhost:8000/login will be routed to the login_user function
    path('login', login_user),
    path('admin/', admin.site.urls),
]
