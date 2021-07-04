from django.urls import path,include
from django.urls.resolvers import URLPattern
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns=[
    path('photo/',views.photo_of_day, name='photoToday'),
    path('photo/',views.past_photo, name='pastPhoto'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)