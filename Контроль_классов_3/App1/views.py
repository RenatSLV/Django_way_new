#     ____   ______ _   __ ___       _____  __  _    __
#    / __ \ / ____// | / //   |     / ___/ / / | |  / /
#   / /_/ // __/  /  |/ // /| |     \__ \ / /  | | / / 
#  / _, _// /___ / /|  // ___ |    ___/ // /___| |/ /  
# /_/ |_|/_____//_/ |_//_/  |_|   /____//_____/|___/   
                                                     

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from App1.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

def dontLogin(request):
    return render(request, 'dontLogin.html')

class listUser(LoginRequiredMixin, ListView):
    template_name = 'index.html'
    model = User
    context_object_name = 'user'
    login_url = 'dontLogin'

class DetailUser(LoginRequiredMixin, DetailView):
    template_name = 'detail.html'
    model = User
    context_object_name = 'user'
    pk_url_kwarg = 'user_id'
    login_url = 'dontLogin'
