# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from .models import Post
from .forms import PostForm

import json
from django.http import HttpResponse


def inicio(request):

	context = {

		'Post': Post.objects.all(),
		'form': PostForm()

	}

	return render(request, 'inicio.html', context)


def CrearPost(request):

	if request.method == 'POST':

		post_texto = request.POST.get('post')

		datos = {}

		crear_post, created = Post.objects.get_or_create(

				usuario = request.user,
				texto = post_texto,

		 	)

		if created:	
			print("Creado")

		datos['resultado']="Post Creado exitosamente"
		datos['pospk'] = crear_post.pk
		datos['texto'] = crear_post.texto
		datos['creado'] = crear_post.creado.strftime('%B %d, %Y %I:%m %p')
		datos['usuario'] = crear_post.usuario.username

		return HttpResponse(

				json.dumps(datos),

				content_type='application/json'
			)

	else:

		return HttpResponse(

				json.dumps({"No funciona" : "Algo esta mal"}),

				content_type = 'application/json'

				)
