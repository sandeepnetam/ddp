from django.db import models

class Year(models.Model):
	"""docstring for year"""
	year = models.CharField(max_length=7, unique=True)

	def __str__(self):
		return '%s' % self.year

class District(models.Model):
	"""docstring for district"""
	district = models.CharField(max_length=40, unique=True)
	def __str__(self):
		return self.district

		
		
class LiveStockGroup(models.Model):
	"""docstring for LiveStockGroup"""
	titel = models.CharField(max_length=50, unique=True)

	def __str__(self):
		return self.titel

class Unit(models.Model):
	"""docstring for Unit"""
	unit = models.CharField(max_length=25, unique=True)

	def __str__(self):
		return self.unit	
		
class LiveStockItem(models.Model):
	"""docstring for LiveStockItem"""
	item = models.CharField(max_length=50, unique=True)
	# unit = models.ForeignKey(Unit, on_delete=False,)
	LiveStockGroup = models.ForeignKey(LiveStockGroup, on_delete=models.CASCADE, null=True, blank=True)
	
	def __str__(self):
		return self.item
		
class LiveStockData(models.Model):
	"""docstring for LiveStockData"""
	DATA_TYPE = (
		('CURRENT', 'CURRENT'),
		('CONSTANT', 'CONSTANT')
		)
	PRODUCTION_TYPE = (('PRODUCTION', 'PRODUCTION'),('INCREMENTS', 'INCREMENTS'))

	Year = models.ForeignKey(Year, on_delete=models.CASCADE)
	LiveStockItem = models.ForeignKey(LiveStockItem, on_delete=models.CASCADE)
	district = models.ForeignKey(District, on_delete=models.CASCADE, null=True)
	DataType = models.CharField(max_length=10, choices=DATA_TYPE)
	production_type = models.CharField(max_length=15, choices=PRODUCTION_TYPE, null=True)
	
	def __str__(self):
		return '%s' % self.LiveStockItem

class ProductionData(models.Model):
	"""docstring for ProductionData"""
	livestockdata = models.ForeignKey('LiveStockData', on_delete=models.CASCADE, null=True, blank=True)
	production = models.DecimalField(max_digits=10, decimal_places=0, null=True,blank=True)
	production_unit = models.ForeignKey('Unit', on_delete=models.CASCADE, null=True, blank=True)

	def __str__(self):
		return '%s' % self.production
		
class PriceData(models.Model):
	"""docstring for ProductionData"""
	livestockdata = models.ForeignKey('LiveStockData', on_delete=models.CASCADE, null=True, blank=True)
	price = models.DecimalField(max_digits=10, decimal_places=0, null=True,blank=True)
	price_unit = models.ForeignKey('Unit', on_delete=models.CASCADE, null=True, blank=True)

	def __str__(self):
		return '%s' % self.production

	
		
