from django.urls import path

from . import views

app_name = 'covidnews'

urlpatterns = [
    path('cnn', views.cnn, name="cnn-news"),
    path('worldometers', views.worldometers, name="worldometers")
]
