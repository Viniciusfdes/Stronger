from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('index/team/', views.sobre, name='sobre'),
    path('index/sup', views.suplementos, name='suplementos')
]
