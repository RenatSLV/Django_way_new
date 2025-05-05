from django.shortcuts import render, redirect
from .forms import PhotoForm
from .models import Photo

def upload_document(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('document_list')
    else:
        form = PhotoForm()
    return render(request, 'upload.html', {'form': form})

def document_list(request):
    photo = Photo.objects.all()
    return render(request, 'document_list.html', {'photo': photo})
