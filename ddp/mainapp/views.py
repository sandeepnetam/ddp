

from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Max, Min, Sum, Count, Q
from django.views.generic import TemplateView
from django.views import View

from .forms import *
from .models import *
from .views import *



class Home(TemplateView):
	"""docstring for Home"""
	tamplate = "ddp/index.html"
	context = {}

	def get(self, request, messages = None):
		ddp_count = ddp.objects.all().count()
		context = {'ddp_count' : ddp_count}
		return render(request, self.tamplate, context)

	def post(self, request, message = None):
		template_name = "ddp/entryddp.html"
		forms = self.DdpModelForm(request.POST or None)
		context = {'forms' : forms, 'messages' : messages}
		if forms.is_valid():
			forms.save()
			forms = self.DdpModelForm()
			data = ddp.objects.all()
			messages = 'Data is Successfuly submitted.'
			alert = 'alert-success'
			context = {'forms' : forms, 'data' : data,   'messages' : messages, 'alert' : alert }

		return render(request, template_name, context)

class Ddp(TemplateView):
	"""docstring for Home"""
	tamplate = "ddp/entryddp.html"
	context = {}

	def get(self, request, messages = None):
		# ddp_count = ddp.objects.all().count()
		context = {
			# 'ddp_count' : ddp_count,
			'forms' : DdpModelForm(),
			}
		return render(request, self.tamplate, context)

	def post(self, request, message = None):
		template_name = "ddp/entryddp.html"
		forms = self.DdpModelForm(request.POST or None)
		context = {'forms' : forms, 'messages' : messages}
		if forms.is_valid():
			forms.save()
			forms = self.DdpModelForm()
			data = ddp.objects.all()
			messages = 'Data is Successfuly submitted.'
			alert = 'alert-success'
			context = {'forms' : forms, 'data' : data,   'messages' : messages, 'alert' : alert }

		return render(request, template_name, context)