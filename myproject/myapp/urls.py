from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('upload/mammogram/', views.upload_mammogram, name='upload_mammogram'),
    path('upload/histopathology/', views.upload_histopathology, name='upload_histopathology'),
    path('upload/ultrasound/', views.upload_ultrasound, name='upload_ultrasound'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
