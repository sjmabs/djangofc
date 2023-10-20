from django.urls import path, include

from .views import index, about, team

urlpatterns = [
    path('', index, name='home'),
    path('team/', team, name='team'),
    path('about/', about, name='about')
]

