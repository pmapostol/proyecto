from django.contrib import admin

# Register your models here.

from .models import Persona, Ubicacion, Tesi, Autor

admin.site.register(Persona),
admin.site.register(Ubicacion),
admin.site.register(Autor),
admin.site.register(Tesi)