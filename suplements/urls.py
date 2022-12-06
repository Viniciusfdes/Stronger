from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('index/', index, name='index'),
    path('index/team/', sobre, name='sobre'),
    path('index/sup', suplementos, name='suplementos'),
    path('index/sup/detalhes/<int:id>', detalhes, name='detalhes')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)









