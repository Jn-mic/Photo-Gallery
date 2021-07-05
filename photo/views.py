# type:ignore
from photo.models import Image
from django.http.response import Http404, HttpResponse
from django.shortcuts import render, redirect
from django.conf import settings
from . import views
from django.conf.urls.static import static
from django.http import HttpResponse
import datetime as dt
from .models import Location, Image, Category



# Create your views here.
# def photo_of_day(request):
#     date=dt.date.today()
#     images=Image.objects.all()
    
#     return render(request,'all-Photos/today-photos.html',{'date':date, 'images':images})

# view function to present  photos from the past days
def photo_list(request):
    images = Image.objects.all()
    context = {
        'images':images
    }
    return render(request,'all-Photos/today-photos.html',context)
    

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

    render(request,'all-Photos/past-photo.html',{'date':date,'image':image})


def photo(request,photo_id):
    try:
        photo= Image.objects.get(id = photo_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-Photos/photo.html", {"photo":photo})

def search_results(request):

    if 'photo' in request.GET and request.GET["photo"]:
        search_term = request.GET.get("photo")
        searched_photo = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all-Photos/search.html',{"message":message,"photos": searched_photo})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-Photos/search.html',{"message":message})