from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, render_to_response
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.template import loader
from django.db.models import Q
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import CreateView, TemplateView


from .models import Persona, Ubicacion, Tesi, Autor




def index(request):
	if request.method == 'GET':
		return render(request, 'buscador/index.html')
	else:	
		username=request.POST['username']
		password=request.POST['password']
		if username and password is not	None:
			#querys =(Q(usuario__contains=username) & Q(contrasena__contains=password))
			#persona = Persona.objects.filter(usuario_contains = username and contrasena_contains=password)
			return render(request, 'buscador/buscador.html')
		else:	
			return render(request, 'buscador/error.html', {'mensaje':'Por favor, introduzca términos validos o no deje vacio el usuario o la contraseña '})


# def auditoria(request):
# 	if request.method == 'GET':
# 		resultados=Tesi.objects.all()
# 		if len(resultados) > 0:
# 		return render(request, 'buscador/auditoria.html', {'resultados':resultados})



def buscarTesis(request):
	if request.method == 'GET':
		# Primera peticion del cliente
		return render(request, 'buscador/buscador.html')
	else:
		# Segunda peticion
		palabras = request.POST['palabras'].split()
		if len(palabras) >= 1:

			resultados = Tesi.objects.filter(nombre__icontains = palabras[0])
			for palabra_adicional in palabras[1:]: # Filtrar por palabras adicionales
				resultados = resultados.filter(palabra_clave__icontains = palabra_adicional)
			if len(resultados) > 0:
				return render(request, 'buscador/resultados.html', {'resultados':resultados})
			else:
				return render(request, 'buscador/error.html', {'mensaje':'No hay resultados'})
		else:
			# Controlar el caso de que el cliente envíe una petición vacía
			return render(request, 'buscador/error.html', {'mensaje':'Por favor, introduce términos de búsqueda'})
