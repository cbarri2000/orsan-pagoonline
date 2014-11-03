from models import Usuario
from django.shortcuts import render_to_response

def v_lista_usuarios(request):
	#usuarios = Usuario.objects.all()
	#return render_to_response('lista_usuarios.html',{'lista':usuarios})
	
	return render_to_response('index.html')