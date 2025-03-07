from django.shortcuts import render, redirect
from django.forms import modelformset_factory

from App1.models import User
from App1.forms import UserForm

def listUsers(request):
    users = User.objects.all()
    context = {
        'users': users,
    }
    return render(request, 'main.html', context)


def addUser(request):
    UserFormSet = modelformset_factory(User, form=UserForm, extra=1, can_delete=True)

    if request.method == 'POST':
        formset = UserFormSet(request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('listUser')
    else:
        formset = UserFormSet(queryset=User.objects.all())

    context = {
        'formset': formset,
    }
    return render(request, 'addUser.html', context)
