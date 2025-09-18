from django.urls import path
from pages.views import home, about, contact,help_views, greeting

urlpatterns = [
    path('home/', home, name='home'),
    path('about/',about, name='about'),
    path('contact/',contact, name='contact'),
    path('help/',help_views, name='help'),
    path('greet/<str:name>/',greeting, name='greet'),
]
