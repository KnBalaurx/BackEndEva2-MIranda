from django.contrib import admin
from clienteApp.models import Cliente

class ClienteAdmin(admin.ModelAdmin):
    list_display= ['nombre', 'apellido' ,'rut', 'email' ,'direccion', 'telefono']

admin.site.register(Cliente, ClienteAdmin)
