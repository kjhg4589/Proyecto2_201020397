from django.shortcuts import HttpResponse
from apps.WebService.Servicios import lista

def usuarios_view(request):
	return HttpResponse(lista.diagrama())
