
from django.db import models
from django.core.validators import RegexValidator

RegexYear = RegexValidator(r'^[20]{2}\d{2}[-][0-9]{2}$', 'Year Pattern is like yyyy-yy')
numeric = RegexValidator(r'^\d+$', 'Only numeric data is allowed.')

class state(models.Model):
	"""docstring for state"""
	name = models.CharField(max_length=100, verbose_name="State", unique=True)
	def __str__(self):
		return '%s' % self.name

class year(models.Model):
	name = models.CharField(max_length=7, verbose_name="Year",validators=[RegexYear], unique=True)
	def __str__(self):
		return '%s' % self.name

class subsector(models.Model):
	SECTOR_CHOICE = (('P', 'PRIMARY'), ('S', 'SECONDARY'), ('T', 'TERTIARY'))
	sector = models.CharField(max_length=1, choices=SECTOR_CHOICE, verbose_name="Sector")
	name = models.CharField(max_length=200, verbose_name="Sub-Sector", unique=True)
	def __str__(self):
		return '%s' % self.name

class district(models.Model):
	"""docstring for district"""
	name = models.CharField(max_length=100, verbose_name="District", unique=True)
	def __str__(self):
		return '%s' % self.name

class baseyear(models.Model):
	"""docstring for baseyear"""
	name = models.CharField(max_length=7, verbose_name="Base Year",validators=[RegexYear], unique=True)
	def __str__(self):
		return '%s' % self.name

class ddp(models.Model):
	PRICE_TYPE = (('CON', 'CONSTANT'), ('CUR', 'CURRENT'))
	baseyear = models.ForeignKey('baseyear', on_delete=models.SET_NULL, verbose_name='Base Year', null=True)

	year = models.ForeignKey('year', on_delete=models.SET_NULL, verbose_name='Year', null=True)
	state = models.ForeignKey('state', on_delete=models.CASCADE, verbose_name='State')
	district = models.ForeignKey('district', on_delete=models.SET_NULL, verbose_name='District', null=True)
	subsector = models.ForeignKey('subsector', on_delete=models.SET_NULL, verbose_name='Sub Sector', null=True)
	price_type = models.CharField(max_length=3, choices=PRICE_TYPE, verbose_name='Price Type')	
	value_in_crore = models.CharField(max_length=8, verbose_name="Value (In Crore Rs.)",validators=[numeric])
	def __str__(self):
		return '%s-%s-%s-%s' % (self.year, self.state, self.district, self.subsector)

