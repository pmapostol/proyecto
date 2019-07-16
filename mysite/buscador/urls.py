from django.urls import  path
from django.conf.urls import include, url

from . import views

app_name = 'buscador'

urlpatterns = [
    path('', views.index, name='index'),
    #path('', 'django.contrib.auth.views.login', {'template_name':'index.html'}, name="login"),
    #path('', views.Index.as_view(), name='index'),
    #path('', views.buscarTesis, name='buscarTesis'),
    url(r'^buscarTesis$', views.buscarTesis, name='buscarTesis'),
    url(r'^auditoria$', views.auditoria, name='auditoria'),

]



