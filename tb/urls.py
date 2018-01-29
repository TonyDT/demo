from django.urls import path,include
from tb import views
urlpatterns = [
    path('index/', views.index),
    path('login/', views.login),
    path('register/', views.register),
    path('logout/', views.logout),
    path(r'^captcha', include('captcha.urls')),
]
