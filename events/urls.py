
from django.urls import path
from .import views

urlpatterns = [
     path('', views.home,name='events/home'),
     path('<str:month>/<int:year>/', views.home,name='events/home'),
     path('events', views.all_events, name='list-events'),
     
]
