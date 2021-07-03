from django.urls import path,include
from django.urls.resolvers import URLPattern


from . import views


URLPattern=[
    path('photo/',views.photo_of_day, name='photoToday'),
    path('photo/',views.past_photo, name='pastPhoto'),

]