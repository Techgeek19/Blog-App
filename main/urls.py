from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('register/',views.register, name='register'),
    path('login/',views.login, name='login'),
    path('post/',views.postview, name='post'),
]
