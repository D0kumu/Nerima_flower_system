from django.urls import path

from . import views

urlpatterns = [
    path('', views.auth, name="auth"),
    path('login', views.login),
    path('signup', views.signup),
]
