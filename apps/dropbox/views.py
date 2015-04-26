from django.shortcuts import render_to_response
from django.template import RequestContext
from apps.dropbox.forms import login, register, crear
from apps.WebService.Servicios import lista

def login_view(request):
	if request.method == "POST":
		formulario = register(request.POST)
		if formulario.is_valid():
			email = formulario.cleaned_data['Email']
			pasword = formulario.cleaned_data['Pasword']
			nodo = lista.obtenerNodo(lista.getCabeza(), email, pasword)
			if lista.login(lista.getCabeza(), email, pasword):
				ctx = {'nodo':nodo}
				return render_to_response("dropbox/dropbox.html", ctx, RequestContext(request))
			else:
				formulario = login()
				ctx = {'form':formulario}
				return render_to_response('dropbox/login.html', ctx, RequestContext(request))
		else:
			formulario = login()
			ctx = {'form':formulario}
			return render_to_response('dropbox/login.html', ctx, RequestContext(request))
	else:
		formulario = login()
		ctx = {'form':formulario}
		return render_to_response('dropbox/login.html', ctx, RequestContext(request))

def inicio_view(request):
	return render_to_response('dropbox/inicio.html', RequestContext(request))

def register_view(request):
	info_enviado = False
	email=""
	pasword=""
	if request.method == "POST":
		formulario = register(request.POST)
		if formulario.is_valid():
			info_enviado = True
			email = formulario.cleaned_data['Email']
			pasword = formulario.cleaned_data['Pasword']
			lista.insertar(email, pasword)
	else:
		formulario = register()
	ctx = {'form':formulario, 'email':email, 'pasword': pasword, 'info_enviado':info_enviado}
	return render_to_response('dropbox/register.html', ctx, RequestContext(request))

def dropbox_view(request):
	return render_to_response('dropbox/dropbox.html', RequestContext(request))

def crear_view(request):
	formulario = crear()
	ctx = {'form':formulario}
	return render_to_response('dropbox/crear.html', ctx, RequestContext(request))

def agregar_view(request):
	return render_to_response('dropbox/agregar.html', RequestContext(request))