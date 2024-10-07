from django.shortcuts import render
from django.http import HttpResponse  
from .models import Task  # Увери се, че импортът е правилен

def index(request):
    tasks = Task.objects.all()

    if not tasks:
        return HttpResponse('<h1>No tasks!</h1>')
    
    result = []

    for task in tasks:
        result.append(f'''
<li>
    <h2>{task.title}</h2>
    <p>{task.description}</p>
</li>
        ''')
    
    ul = f'<ul>{"".join(result)}</ul>'  # Коригирано

    content = f'''
    <h1>{len(tasks)} Tasks</h1>
    {ul}
    '''

    return HttpResponse(content)
