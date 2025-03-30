from django.shortcuts import render, redirect

from App1.models import Client
from App1.forms import AddClientForm

def add_Client(request):
    if request.method == 'POST':
        form = AddClientForm(request.POST)
        if form.is_valid():
            Client.objects.create(
                name=form.cleaned_data['name'],
                age=form.cleaned_data['age']
            )
            return redirect('home')

    else:
        form = AddClientForm()
    
    context = {
        'form': form
    }
    return render(request, 'addClient.html', context)

def home(request):
    clients = Client.objects.all()
    context = {
        'clients': clients
    }
    return render(request, 'home.html', context)
