

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
		context = {}
		return render(request, self.tamplate, context)

