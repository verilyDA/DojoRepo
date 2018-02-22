from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^new$', views.new),
    url(r'^create$', views.create),     # This line has changed!
    url(r'^[0-9]$', views.number),
    url(r'^[0-9]/edit$', views.numEdit),
    url(r'^[0-9]/delete$', views.numDel),
]
