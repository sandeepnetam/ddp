import csv, io
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.db.models import Max, Min, Sum, Count, Q
from .forms import *
from .models import *
from .views import *
from django.views import View
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

def LiveStockBaseView(request):
	template_name = "livestock/livestockbase.html"

	context = {}
	return render(request, template_name, context)

# class LiveStockView(TemplateView):
# 	"""docstring for LiveStockView"""
# 	template_name = "livestock/LivestockDataEntry.html"
# 	form_class = LiveStockDataForm
# 	data = LiveStockData.objects.all()
	
# 	def get(self, request):
# 		forms = self.form_class()
		
# 		context = {'forms' : forms, 'data' : self.data }

# 		return render(request, self.template_name, context)

# 	def post(self, request):
# 		forms = self.form_class(request.POST or None)
# 		context = {'forms' : forms}
# 		if forms.is_valid():
# 			forms.save()
# 			data = LiveStockData.objects.all()
# 			messages = 'Data is Successfuly submitted.'
# 			context = {'forms' : forms, 'data' : data, 'messages' : messages}
# 		return render(request, self.template_name, context)

def LiveStockData_list(request):
	LiveStockData_list = LiveStockData.objects.all()
	return render(request, "livestock/LivestockList.html", {'LiveStockData_list' : LiveStockData_list})	



# class LiveStockListView(View):
# 	"""docstring for LiveStockView"""
# 	model = LiveStockData
# 	template_name = "livestock/LivestockList.html"

	# def get(self, request):
	# 	LiveStockData_list = LiveStockData.objects.all()
	# 	return render(request, "livestock/LivestockList.html", {'LiveStockData_list' :self.get_queryset()})	

	# def get_queryset(request):
	# 	return LiveStockData.objects.all()

class YearListView(ListView):
	"""docstring for Year View"""
	queryset = Year.objects.all()

class DistrictListView(ListView):
	"""docstring for District View"""
	queryset = District.objects.all()

class LiveStockGroupListView(ListView):
	"""docstring for Group View"""
	queryset = LiveStockGroup.objects.all()

class LiveStockItemListView(ListView):
	"""docstring for LiveStockView"""
	queryset = LiveStockItem.objects.all()


class LiveStockDataListView(ListView):
	"""docstring for LiveStockView"""
	queryset = LiveStockData.objects.all()
	
class LiveStockDataDetailView(DetailView):
	"""docstring for LiveStockView"""
	queryset = LiveStockData.objects.all()
	

class LiveStockDistrictView(TemplateView):
	"""docstring for LiveStockView"""
	template_name = "livestock/entry.html"
	form_class = DistrictForm
	data = District.objects.all()

	def get(self, request, messages = None):
		forms = self.form_class()
		data = District.objects.all()
		context = {'forms' : forms, 'data' : data, 'messages': messages}
		return render(request, self.template_name, context)

	def post(self, request):
		forms = self.form_class(request.POST or None)
		context = {'forms' : forms, 'data' : self.data }
		if forms.is_valid():
			forms.save()
			data = District.objects.all()
			messages = 'Data is Successfuly submitted.'
			context = {'forms' : forms, 'data' : data,   'messages' : messages}

		return render(request, self.template_name, context)

	def DeleteDistrictView(request, pk=None):
		link = "/livestock/entry/district/"
		instance = get_object_or_404(District, pk=pk)
		instance.delete()
		messages = 'Data is Successfuly Deleted.'
		return redirect( link , kwargs={ 'messages': messages })

	def UpdateDistrictView(request, pk=None):
		link = "/livestock/entry/district/"
		instance = get_object_or_404(District, pk=pk)
		forms = DistrictForm(request.POST or None, instance=instance)
		# data = District.objects.all()
		context = {'forms' : forms }
		if forms.is_valid():
			instance = forms.save(commit=False)
			instance.save()
			# data = District.objects.all()
			messages = 'Data is Successfuly submitted.'
			context = {'forms' : forms,   'messages' : messages}
			
			return redirect( link , kwargs={ 'messages': messages })

		return render(request, "livestock/entry.html", context)


class LiveStockYearView(TemplateView):
	"""docstring for LiveStockView"""
	template_name = "livestock/entry.html"
	form_class = YearForm
	data = Year.objects.all()

	def get(self, request):
		forms = self.form_class()
		data = Year.objects.all()
		context = {'forms' : forms, 'data' : data }
		return render(request, self.template_name, context)

	def post(self, request):
		forms = self.form_class(request.POST or None)
		context = {'forms' : forms, 'data' : self.data }
		if forms.is_valid():
			forms.save()
			data = Year.objects.all()
			messages = 'Data is Successfuly submitted.'
			context = {'forms' : forms, 'data' : data,   'messages' : messages}

		return render(request, self.template_name, context)

	def DeleteYearView(request, pk=None):
		link = "/livestock/entry/year/"
		instance = get_object_or_404(Year, pk=pk)
		instance.delete()
		messages = 'Data is Successfuly Deleted.'
		return redirect( link , kwargs={ 'messages': messages })

	def UpdateYearView(request, pk=None):
		link = "/livestock/entry/year/"
		instance = get_object_or_404(Year, pk=pk)
		forms = YearForm(request.POST or None, instance=instance)
		# data = Year.objects.all()
		context = {'forms' : forms}
		if forms.is_valid():
			instance = forms.save(commit=False)
			instance.save()
			# data = Year.objects.all()
			messages = 'Data is Successfuly submitted.'
			context = {'forms' : forms,   'messages' : messages}
			
			return redirect( link , kwargs={ 'messages': messages })

		return render(request, "livestock/entry.html", context)

	

class LiveStockGroupView(TemplateView):
	"""docstring for LiveStockView"""
	template_name = "livestock/entry.html"
	form_class = LiveStockGroupForm
	data = LiveStockGroup.objects.all()

	def get(self, request):
		forms = self.form_class()
		data = LiveStockGroup.objects.all()
		context = {'forms' : forms, 'data' : data }
		return render(request, self.template_name, context)

	def post(self, request):
		forms = self.form_class(request.POST or None)
		context = {'forms' : forms, 'data' : self.data }
		if forms.is_valid():
			forms.save()
			data = LiveStockGroup.objects.all()
			messages = 'Data is Successfuly submitted.'
			context = {'forms' : forms, 'data' : data,   'messages' : messages}

		return render(request, self.template_name, context)

	def DeleteGroupView(request, pk=None):
		link = "/livestock/entry/livestockgroup/"
		instance = get_object_or_404(LiveStockGroup, pk=pk)
		instance.delete()
		messages = 'Data is Successfuly Deleted.'
		return redirect( link , kwargs={ 'messages': messages })

	def UpdateGroupView(request, pk=None):
		link = "/livestock/entry/livestockgroup/"
		instance = get_object_or_404(LiveStockGroup, pk=pk)
		forms = LiveStockGroupForm(request.POST or None, instance=instance)
		# data = LiveStockGroup.objects.all()
		context = {'forms' : forms}
		if forms.is_valid():
			instance = forms.save(commit=False)
			instance.save()
			# data = LiveStockGroup.objects.all()
			messages = 'Data is Successfuly submitted.'
			context = {'forms' : forms,   'messages' : messages}
			
			return redirect( link , kwargs={ 'messages': messages })

		return render(request, "livestock/entry.html", context)

class UnitView(TemplateView):
	"""docstring for LiveStockView"""
	template_name = "livestock/entry.html"
	form_class = UnitForm
	data = Unit.objects.all()

	def get(self, request):
		forms = self.form_class()
		data = Unit.objects.all()
		context = {'forms' : forms, 'data' : data }
		return render(request, self.template_name, context)

	def post(self, request):
		forms = self.form_class(request.POST or None)
		context = {'forms' : forms, 'data' : self.data }
		if forms.is_valid():
			forms.save()
			data = Unit.objects.all()
			messages = 'Data is Successfuly submitted.'
			context = {'forms' : forms, 'data' : data,   'messages' : messages}

		return render(request, self.template_name, context)

	def DeleteUnitView(request, pk=None):
		link = "/livestock/entry/unit/"
		instance = get_object_or_404(Unit, pk=pk)
		instance.delete()
		messages = 'Data is Successfuly Deleted.'
		return redirect( link , kwargs={ 'messages': messages })

	def UpdateUnitView(request, pk=None):
		link = "/livestock/entry/unit/"
		instance = get_object_or_404(Unit, pk=pk)
		forms = UnitForm(request.POST or None, instance=instance)
		# data = Unit.objects.all()
		context = {'forms' : forms }
		if forms.is_valid():
			instance = forms.save(commit=False)
			instance.save()
			# data = Unit.objects.all()
			messages = 'Data is Successfuly submitted.'
			context = {'forms' : forms,   'messages' : messages}
			
			return redirect( link , kwargs={ 'messages': messages })

		return render(request, "livestock/entry.html", context)


class LiveStockItemView(TemplateView):
	"""docstring for LiveStockView"""
	template_name = "livestock/entry.html"
	form_class = LiveStockItemForm
	data = LiveStockItem.objects.all()

	def get(self, request):
		forms = self.form_class()
		data = LiveStockItem.objects.all()
		context = {'forms' : forms, 'data' : data }
		return render(request, self.template_name, context)

	def post(self, request):
		forms = self.form_class(request.POST or None)
		context = {'forms' : forms, 'data' : self.data }
		if forms.is_valid():
			forms.save()
			data = LiveStockItem.objects.all()
			messages = 'Data is Successfuly submitted.'
			context = {'forms' : forms, 'data' : data,   'messages' : messages}

		return render(request, self.template_name, context)

	def DeleteItemView(request, pk=None):
		link = "/livestock/entry/item/"
		instance = get_object_or_404(LiveStockItem, pk=pk)
		instance.delete()
		messages = 'Data is Successfuly Deleted.'
		return redirect( link , kwargs={ 'messages': messages })

	def UpdateItemView(request, pk=None):
		link = "/livestock/entry/item/"
		instance = get_object_or_404(LiveStockItem, pk=pk)
		forms = LiveStockItemForm(request.POST or None, instance=instance)
		# data = LiveStockItem.objects.all()
		context = {'forms' : forms }
		if forms.is_valid():
			instance = forms.save(commit=False)
			instance.save()
			# data = LiveStockItem.objects.all()
			messages = 'Data is Successfuly submitted.'
			context = {'forms' : forms,   'messages' : messages}
			
			return redirect( link , kwargs={ 'messages': messages })

		return render(request, "livestock/entry.html", context)

class LiveStockDataView(TemplateView):
	"""docstring for LiveStockView"""
	template_name = "livestock/database_item_entry.html"
	form_class = LiveStockDataForm
	form_production = ProductionDataForm 
	form_price = PriceDataForm
	data = LiveStockData.objects.all()

	def get(self, request):
		forms = self.form_class()
		forms_production = self.form_production()
		forms_price = self.form_price()
		data = LiveStockData.objects.all()
		context = {	'forms' : forms, 
					'data' : data, 
					'form_production' : forms_production ,
					'form_price' : forms_price
					}
		return render(request, self.template_name, context)

	def post(self, request):
		forms = self.form_class(request.POST or None)
		forms_production = self.form_production(request.POST or None)
		forms_price = self.form_price(request.POST or None)

		context = {	'forms' : forms, 
					'data' : data, 
					'form_production' : forms_production ,
					'form_price' : forms_price
					}

		if forms.is_valid() and forms_production.is_valid() and forms_price.is_valid():
			forms.save()
			data = LiveStockData.objects.all()
			messages = 'Data is Successfuly submitted.'
			context = {	'forms' : forms, 
						'data' : data,   
						'messages' : messages, 
						'form_production' : forms_production ,
						'form_price' : forms_price
						}

		return render(request, self.template_name, context)

	def DeleteDataView(request, pk=None):
		link = "/livestock/entry/livestockdata/"
		instance = get_object_or_404(LiveStockData, pk=pk)
		instance.delete()
		messages = 'Data is Successfuly Deleted.'
		return redirect( link , kwargs={ 'messages': messages })

	def UpdateDataView(request, pk=None):
		link = "/livestock/entry/livestockdata/"
		instance = get_object_or_404(LiveStockData, pk=pk)
		forms = LiveStockDataForm(request.POST or None, instance=instance)
		# data = LiveStockData.objects.all()
		context = {'forms' : forms}
		if forms.is_valid():
			instance = forms.save(commit=False)
			instance.save()
			# data = LiveStockData.objects.all()
			messages = 'Data is Successfuly submitted.'
			context = {'forms' : forms,   'messages' : messages}
			
			return redirect( link , kwargs={ 'messages': messages })

		return render(request, "livestock/entry.html", context)





