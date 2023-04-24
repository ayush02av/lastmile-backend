from django.urls import path
from api.views import views_user

urlpatterns = [
    path('', views_user.user.as_view(),),
    path('add/', views_user.add.as_view(),),
    path('start/', views_user.start.as_view(),),
    path('join/', views_user.join.as_view(),),
]