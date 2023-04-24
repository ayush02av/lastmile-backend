from django.urls import path
from api.views import views_event

urlpatterns = [
    path('', views_event.events.as_view(), name='events'),
]