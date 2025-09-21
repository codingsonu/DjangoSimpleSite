# from django.shortcuts import render
# from django.http import JsonResponse
# from rest_framework.decoratores import api_view
# # Create your views here.
# def home(request):
#     return  JsonResponse({'message': 'welcome to home page'})

# def about(request):
#     return JsonResponse({
#         'message': 'welcome to about page'
#     })
# def contact(request):
#     return JsonResponse({
#         'message': 'welcome to contact page'
#     })

# def help_views(request):
#     return JsonResponse({
#          "message": "this is help page",
#          "status": "active"
#     })

# def greeting(request, name):
#     return JsonResponse({
#          "message": f"Hello, {name}!"
    # })


from rest_framework.decorators import api_view
from rest_framework.response import Response

tasks = [
        {'id': 1, 'title': 'Task 1', 'completed': False},
        {'id': 2, 'title': 'Task 2', 'completed': True},
        {'id': 3, 'title': 'Task 3', 'completed': False},
    ]

@api_view(['GET'])
def task_list(request):
    return Response({'task' : tasks})

@api_view(['POST'])
def add_task(request):
    data = request.data
    new_task = {
        'id': len(tasks)+1,
        'title': data.get('title'),
        'completed': data.get('completed', False)
    }
    tasks.append(new_task)
    return Response({'message': 'task added successfully', 'task':new_task})

# pages/views.py (ya kisi app me jahan comfortable ho)
from django.shortcuts import render

def serve_react(request):
    return render(request, 'index.html')
