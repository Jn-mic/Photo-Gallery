from django.http.response import Http404, HttpResponse,40
from django.shortcuts import render, redirect
from django.conf import settings
from . import views
from django.conf.urls.static import static
from django.http import HttpResponse
from datetime import dt


# Create your views here.
def photo_of_day(request):
    date=dt.date.today()

    render(request,'all-photos/today-photos.html',{'date':date,})

# view function to present  photos from the past days
def past_photo(request,past_date):
    try:
        # Convert data from string url
        date= dt.datetime.strptime(past_date,'%Y-%m-%d').date()
    except ValueError:
        #Raise 404 error when valueError is thrown
        raise Http404()
        assert False
    if date == dt.date.today():
        return redirect(photo_of_day)


    render(request,'past-photo.html')
