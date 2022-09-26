from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from .forms import *


def registro(request):
	if request.method == 'POST':
		form = Registro(request.POST)
		if form.is_valid():
			form.save()
			usuario = form.cleaned_data.get('username')
			password= form.cleaned_data.get('password1')
			cuenta= authenticate(username=usuario, password=password)
			login(request,cuenta)
			return redirect ('index')
		else:
			return HttpResponse('las contraseñas no son validas')
	else:
		form = Registro()
		return render(request, 'registro.html', { 'form' : form })





