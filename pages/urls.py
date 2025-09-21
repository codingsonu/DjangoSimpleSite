from django.urls import path, re_path
from pages.views import task_list, add_task,serve_react

urlpatterns = [
    # path('home/', home, name='home'),
    # path('about/',about, name='about'),
    # path('contact/',contact, name='contact'),
    # path('help/',help_views, name='help'),
    # path('greet/<str:name>/',greeting, name='greet'),
    path('tasks/', task_list, name='task_list'),
    path('tasks/add/', add_task, name='add_task'),
    re_path(r'^.*$', serve_react, name='react-app'),
]
