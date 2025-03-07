from django.shortcuts import render
from App1.models import Users
from django.views.generic import CreateView, DetailView, ListView
from django.urls import reverse_lazy

#     ____   ______ _   __ ___       _____  __  _    __
#    / __ \ / ____// | / //   |     / ___/ / / | |  / /
#   / /_/ // __/  /  |/ // /| |     \__ \ / /  | | / / 
#  / _, _// /___ / /|  // ___ |    ___/ // /___| |/ /  
# /_/ |_|/_____//_/ |_//_/  |_|   /____//_____/|___/  

class CreateUser(CreateView):
    model = Users
    fields = ['name', 'email', 'password']
    template_name = 'Home.html'
    success_url = reverse_lazy('CreateUser')

class ListUsers(ListView):
    model = Users
    template_name = 'listUsers.html'
    context_object_name = 'Users'


def detailUser(request, *args, **kwargs):
    context = {}
    if request.method == 'POST':
        UserId = request.POST.get('id')
        user = Users.objects.get(id=UserId)
        context['use'] = user
    return render(request, 'detailUser.html', context)
