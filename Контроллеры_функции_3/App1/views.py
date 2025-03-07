from django.shortcuts import render, redirect
from django.http import Http404
from App1.models import *
# Create your views here.

def index(request):
    if request.method == "POST":
        username = request.POST.get('username')
        userpassword = request.POST.get('userpassword')

        if username and userpassword:
            User.objects.create(name=username, password=userpassword)
            return redirect(index2)
        else:
            raise Http404()
    return render(request, 'index.html')


def index2(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'index2.html', context)