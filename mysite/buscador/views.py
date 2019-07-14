from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, render_to_response
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.template import loader
from django.db.models import Q

from .models import Persona, Ubicacion, Tesi, Autor




def index(request):
    return HttpResponse("Hola, mundo. Está en el índice de encuestas.")


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
				resultados = resultados.filter(nombre__icontains = palabra_adicional)
			if len(resultados) > 0:
				return render(request, 'buscador/resultados.html', {'resultados':resultados})
			else:
				return render(request, 'buscador/error.html', {'mensaje':'No hay resultados'})
		else:
			# Controlar el caso de que el cliente envíe una petición vacía
			return render(request, 'buscador/error.html', {'mensaje':'Por favor, introduce términos de búsqueda'})
