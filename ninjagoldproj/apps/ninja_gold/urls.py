from django.conf.urls import url
from django.urls import path
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    path('process_gold/<str:loc>', views.process),
    url(r'^reset$', views.reset),
] 