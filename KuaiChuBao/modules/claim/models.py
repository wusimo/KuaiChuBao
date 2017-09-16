# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class UserInfo(models.Model):
	name = models.CharField(max_length=200, null=True, blank=True)
	phone = models.CharField(max_length=200, null=True, blank=True)
	national_id_number = models.CharField(max_length=200, unique=True)
	driver_license_number = models.CharField(max_length=200, null=True, blank=True)

	national_id_top = models.ImageField(upload_to='users/national_id', null=True, blank=True)
	national_id_down = models.ImageField(upload_to='users/national_id', null=True, blank=True)
	driver_license_top = models.ImageField(upload_to='users/driver_license', null=True, blank=True)
	driver_license_down = models.ImageField(upload_to='users/driver_license', null=True, blank=True)
	road_worthiness_certificate_top = models.ImageField(upload_to='users/road_worthiness_certificate', null=True, blank=True)
	road_worthiness_certificate_down = models.ImageField(upload_to='users/road_worthiness_certificate', null=True, blank=True)

	# relations
	# 1. claims

	def __str__(self):
		return self.name


class InsuranceCompany(models.Model):
	name = models.CharField(max_length=200)
	phone = models.CharField(max_length=200)
	url = models.CharField(max_length=200, null=True, blank=True)
	logo = models.ImageField(upload_to='companies_logo/', null=True, blank=True)

	# relations
	# 1. claims

	def __str__(self):
		return self.name


class Location(models.Model):
	pass

class Insurance(models.Model):
	A,B,C,D,E = 0,1,2,3,4
	THIRD_PARTY_CHOICES = (
		(A,'1.1万元'),
		(B,'2.2万元'),
		(C,'3.3万元'),
		(D,'4.5万元'),
		(E,'5.1万元')
		)

	a,b,c,d,e,f,g,h,i,j,k,l,m = 0,1,2,3,4,5,6,7,8,9,10,11,12,13


	INSURANCE_COMPANY_CHOICES = (
		(a,'人保财险'),
		(b,'平安财险'),
		(c,'太保财险'),
		(d,'阳光财险'),
		(e,'大地财险'),
		(f,'国寿财险'),
		(g,'华安财险'),
		(h,'鼎和财险'),
		(i,'安诚财险'),
		(j,'锦泰财险'),
		(k,'永诚财险'),
		(l,'国元财险'),
		(m,'永安财险')

		)

	# basic insurance
	obligatory = models.BooleanField() #机动车交通事故责任强制保险 
	tax = models.BooleanField()# 车船使用税（按照汽车排量征收）

	loss = models.BooleanField() #机动车损失保险
	third_party = models.IntegerField(default = A,choices = THIRD_PARTY_CHOICES)#机动车第三者责任保险  
	people_in_car = models.IntegerField(default = A,choices = THIRD_PARTY_CHOICES)#机动车车上人员责任保险                     
	stolen_insurance = models.BooleanField() #机动车全车盗抢保险

	# 附加险

	single_glass_broken = models.BooleanField()#玻璃单独破碎险                     
	natural_loss = models.BooleanField() #自然损失险                           □
    new_add_equip = models.BooleanField()#新增加设备损失险                 
	scratch = models.BooleanField()#车身划痕损失险               
	engine_water = models.BooleanField()#发动机涉水损失险                                       
	while_repair = models.BooleanField()#修理期间费用补偿险                                    
	cargo = models.BooleanField()# 车上货物责任险                                          
	mental_loss = models.BooleanField()#精神损害抚慰金责任险                                
	frachise = models.BooleanField()#不计免赔率险                                             
	third_party_missing = models.BooleanField()#机动车损失保险无法找到第三方特约险         
	assign_repair = models.BooleanField()#指定修理厂险                                            

	insurance_company = models.IntegerField(default=a,choices =INSURANCE_COMPANY_CHOICES )

class Claim(models.Model):
	TYPE_CHOICES = (
		(1, '单车事故'),
		(2, '两车刮擦事故'),
		(3, '两车追尾事故'),
	)
	company = models.ForeignKey(InsuranceCompany, related_name='claims',null = True)
	plate = models.CharField(max_length=200,null = True)
	time = models.DateTimeField(max_length=200,null = True)
	location = models.CharField(max_length=200,null = True)
	user = models.ForeignKey(UserInfo, related_name='claims',null = True)
	# time stamp
	created = models.DateTimeField(auto_now_add=True)

	# relations
	# 1. images

	def __str__(self):
		# this has some problem
		return self.user.name + ' ' #+ self.created.strftime('%Y-%m-%d %H:%M')


class Image(models.Model):
	claim = models.ForeignKey(Claim, related_name='images')
	image = models.ImageField(upload_to='claims')
	# time stamp
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.claim.user.name + ' ' + self.created.strftime('%Y-%m-%d %H:%M') + ' image'
