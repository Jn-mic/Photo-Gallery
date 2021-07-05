from django.urls import path,include
from django.urls.resolvers import URLPattern
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns=[
    path('photo_list',views.photo_list, name='photo_list'),
    path('photo/<str:photo_id>/',views.photo, name='search_photo'),
    path('search/',views.search_results, name='search_results'),
    


]

