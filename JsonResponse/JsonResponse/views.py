from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_http_methods

def jsonresponse(request):
    data = {'name': 'Renat',
            'age': 18
    }
    return JsonResponse(data)
    
def redirectfunc(request):
    return redirect('index')

def index(request):
    return render(request, 'index.html')

@require_http_methods(['GET'])
def GetMethod(request):
    return HttpResponse('Только GET запросы разрешены')
