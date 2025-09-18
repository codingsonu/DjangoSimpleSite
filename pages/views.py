from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
def home(request):
    return  JsonResponse({'message': 'welcome to home page'})

def about(request):
    return JsonResponse({
        'message': 'welcome to about page'
    })
def contact(request):
    return JsonResponse({
        'message': 'welcome to contact page'
    })

def help_views(request):
    return JsonResponse({
         "message": "this is help page",
         "status": "active"
    })

def greeting(request, name):
    return JsonResponse({
         "message": f"Hello, {name}!"
    })