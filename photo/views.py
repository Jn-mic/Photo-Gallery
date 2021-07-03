from django.http.response import HttpResponse
from django.shortcuts import render
from django.conf import settings
from . import views
from django.conf.urls.static import static
from django.http import HttpResponse
from datetime import dt


# Create your views here.
def photo_of_day(request):
    date=dt.date.today()

    render(request,'welcome.html')

def past_photo(request):
    past= dt.date()

    render(request,'past-photo.html')
