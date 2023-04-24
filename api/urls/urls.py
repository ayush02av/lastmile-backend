from django.urls import path, include

urlpatterns = [
    path('auth/', include('api.urls.urls_auth')),
    path('skill/', include('api.urls.urls_skill')),
    path('user/', include('api.urls.urls_user')),
]