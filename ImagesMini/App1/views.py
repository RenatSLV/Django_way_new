from django.shortcuts import render, redirect
from App1.models import UploadedImage
from django.core.files.base import ContentFile
import os

def upload_image(request):
    if request.method == 'POST' and request.FILES['image']:
        img_file = request.FILES['image']
        data = img_file.read()

        filename = os.path.basename(img_file.name)
        instance = UploadedImage(title=request.POST.get('title'))
        instance.image.save(filename, ContentFile(data), save=True)

        return redirect('show_images')
    return render(request, 'upload.html')

def show_images(request):
    images = UploadedImage.objects.all()
    return render(request, 'gallery.html', {'images': images})
