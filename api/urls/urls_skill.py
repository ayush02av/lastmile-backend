from django.urls import path
from api.views import views_skill

urlpatterns = [
    path('', views_skill.skills.as_view(), name='skills'),
    path('<str:skill>/', views_skill.skill_user.as_view(), )
]