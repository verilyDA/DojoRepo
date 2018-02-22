from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^process/(?P<source>\w+)$', views.gold),
    url(r'^clear$', views.clear),
]
