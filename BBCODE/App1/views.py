from django.shortcuts import render, redirect
from .models import BBCodeContent

def save_bbcode(request):
    if request.method == 'POST':
        bbcode_input = request.POST.get('bbcode_input')
        if bbcode_input:
            BBCodeContent.objects.create(content=bbcode_input)
            return redirect('show_bbcode')  # Название урла
    return render(request, 'bbcode_form.html')

def show_bbcode(request):
    bbcode_entries = BBCodeContent.objects.all()
    return render(request, 'show_bbcode.html', {'bbcode_entries': bbcode_entries})
