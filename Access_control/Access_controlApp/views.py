from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth import authenticate, login, logout


def CreateGroupView(request):
    if request.method == 'POST':
        group_name = request.POST.get('name')
        selected_permissions = request.POST.getlist('permission')

        if not group_name:
            return render(request, 'createGroup.html', {'error': 'Insert name Group'})

        group = Group.objects.create(name=group_name)

        if selected_permissions:
            permissions = Permission.objects.filter(id__in=selected_permissions)
            group.permissions.set(permissions)

        return redirect('list_user')

    all_permisions = Permission.objects.all()
    context = {
        'all_permisions': all_permisions
    }
    return render(request, 'createGroup.html', context)


def ListUserView(request):
    users = User.objects.prefetch_related('groups').all()
    context = {
        'users': users
    }
    return render(request, 'listUser.html', context)


def CreateUserView(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        user_password = request.POST.get('user_password')
        user_group = request.POST.get('user_group')

        user = User.objects.create_user(username=user_name, password=user_password)
        group = Group.objects.get(name=user_group)
        user.groups.add(group)
        
        return redirect('LogIn')
    
    all_Groups = Group.objects.all()
    context = {
        'all_Groups': all_Groups
    }
    return render(request, 'createUSer.html', context)


def LogInView(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        user_password = request.POST.get('user_password')

        user = authenticate(request, username=user_name, password=user_password)

        if user is not None:
            login(request, user)
            return redirect('list_user')
        else:
            return redirect('create_user')
        
    return render(request, 'LogIn.html')

def LogOutView(request):
    logout(request)
    return redirect('list_user')

        
