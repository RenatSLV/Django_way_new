from django.shortcuts import render, redirect
from FormsApp.models import IceCream
from FormsApp.forms import IceCreamForm

def listIceCream(request):
    iceCreams = IceCream.objects.all()
    context = {
        'iceCreams': iceCreams
    }
    return render(request, 'list.html', context)

def addIceCream(request):
    if request.method == 'POST':
        icf = IceCreamForm(request.POST)
        if icf.is_valid():
            icf.save()
            return redirect('list')
        else:
            context = {'form': icf}
            return render(request, 'add.html', context)
    else:
        icf = IceCreamForm()

        context = {'form': icf}
        return render(request, 'add.html', context)