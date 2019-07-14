from django.urls import  path
from django.conf.urls import url

from . import views

app_name = 'buscador'

urlpatterns = [
    path('', views.index, name='index'),
    #path('', views.Index.as_view(), name='index'),
    #path('', views.buscarTesis, name='buscarTesis'),
    url(r'^buscarTesis$', views.buscarTesis, name='buscarTesis')
    

]