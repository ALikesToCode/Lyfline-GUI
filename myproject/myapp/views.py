from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import MammogramForm, HistopathologyForm, UltrasoundForm
import os
from django.conf import settings

def index(request):
    return render(request, 'index.html')

def upload_mammogram(request):
    return handle_upload(request, MammogramForm)

def upload_histopathology(request):
    return handle_upload(request, HistopathologyForm)

def upload_ultrasound(request):
    return handle_upload(request, UltrasoundForm)

def handle_upload(request, form_class):
    if request.method == 'POST':
        form = form_class(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            with open(os.path.join(settings.MEDIA_ROOT, file.name), 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            return JsonResponse({'message': 'File uploaded successfully'})
        else:
            return JsonResponse({'message': 'Invalid file'}, status=400)
    return JsonResponse({'message': 'Invalid request'}, status=400)
