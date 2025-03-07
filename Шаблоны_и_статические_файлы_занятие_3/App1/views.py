from django.shortcuts import render
from App1.models import Film

def base_views(request):
    films = Film.objects.all()
    context = {
        'films': films
    }
    return render(request, 'base.html', context)
