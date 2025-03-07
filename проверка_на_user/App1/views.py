from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return HttpResponse('hello world')
    else:
        return redirect('index2')

def index2(request):
    return render(request, 'index.html')