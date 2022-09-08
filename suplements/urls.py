from xml.dom.minidom import Document
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('index/', views.index, name='index'),
    path('index/team/', views.sobre, name='sobre'),
    path('index/sup', views.suplementos, name='suplementos'),
    path('index/sup/detalhes/<int:id>', views.detalhes, name='detalhes')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
