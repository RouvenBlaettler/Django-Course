from django.shortcuts import render


def task_view(request):
    tasks = [
        'Buy apples',
        'Write tests',
        'Deploy app',
    ]
    context = {'tasks': tasks}
    return render(request, 'tasks.html', context)
