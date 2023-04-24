from django.urls import path
from api.views import views_auth

urlpatterns = [
    path("login/", views_auth.login, name="login"),
    path("logout/", views_auth.logout, name="logout"),
    path("callback/", views_auth.callback, name="callback"),
    path("handler/", views_auth.handler, name="handler"),
]