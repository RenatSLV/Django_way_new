from django.shortcuts import render

from App1.models import Coment

def list_coments(request):
    coments = Coment.objects.all()
    context = {
        'coments': coments
    }
    return render(request, 'list_coments.html', context)
