from django import forms
# from crispy_forms.helper import FormHelper
from .models import *

class YearForm(forms.ModelForm):
	class Meta:
		model = Year
		fields = ['year']
		widgets = {'year': forms.TextInput(attrs={'class':'input'})}

class DistrictForm(forms.ModelForm):
	class Meta:
		model = District
		fields = ['district']
		widgets = {'district': forms.TextInput(attrs={'class':'input'})}

class LiveStockGroupForm(forms.ModelForm):
	class Meta:
		model = LiveStockGroup
		fields = ['titel']
		widgets = {'titel': forms.TextInput(attrs={'class':'input'})}

class UnitForm(forms.ModelForm):
	class Meta:
		model = Unit
		fields = ['unit']
		widgets = {'unit': forms.TextInput(attrs={'class':'input'})}

class LiveStockItemForm(forms.ModelForm):
	class Meta:
		model = LiveStockItem
		fields = ['item', 'LiveStockGroup']
		widgets = {
					'item': forms.TextInput(attrs={'class':'input'}),
				
					}

class LiveStockDataForm(forms.ModelForm):
	class Meta:
		model = LiveStockData
		fields = [
					'Year',
					'district',
					
					
					'LiveStockItem',
					'DataType',
					
					]

		# widgets = {
		# 			'Year': forms.TextInput(attrs={'class':'input'}),
		# 			'unit': forms.TextInput(attrs={'class':'input'})
		# 			}

class ProductionDataForm(forms.ModelForm):
	class Meta:
		model = ProductionData
		fields = [
					'production',
					'production_unit'
					]

class PriceDataForm(forms.ModelForm):
	class Meta:
		model = PriceData
		fields = [
					'price',
					'price_unit'
					]