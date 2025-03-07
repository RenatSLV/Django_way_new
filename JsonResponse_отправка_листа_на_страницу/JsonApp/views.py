from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    lst = [n for n in range(1, 101)]
    return JsonResponse(lst, safe=False)

