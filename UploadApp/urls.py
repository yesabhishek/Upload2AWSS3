  
from django.urls import path
from UploadApp.views import Upload

app_name = 'UploadApp'

urlpatterns = [
    path('', Upload.as_view(), name='upload'),
]