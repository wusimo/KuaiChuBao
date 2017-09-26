# -*- coding: utf-8 -*-
from django import forms
from .models import  Image,Insurance #Post,
from django.utils.translation import ugettext_lazy as _



class PostForm(forms.ModelForm):
 	title = forms.CharField(max_length=128, label="Name")

 	# body = forms.CharField(max_length=245, label="Item Description.")
 	class Meta:
 		#model = Post
 		fields = ('title',)

class InsuranceForm(forms.ModelForm):



	class Meta:
		model = Insurance
		fields = ('obligatory','tax','loss','third_party','people_in_car','stolen_insurance','single_glass_broken',
			'natural_loss','new_add_equip','scratch','engine_water','while_repair','cargo','mental_loss','frachise',
			'third_party_missing','assign_repair','insurance_company')

		labels = {
            'obligatory': '机动车交通事故责任强制保险',
            'tax':'车船使用税（按照汽车排量征收）',
            'loss':'机动车损失保险',
            'third_party':'机动车第三者责任保险 ',
            'people_in_car':'机动车车上人员责任保险',
            'stolen_insurance':'机动车全车盗抢保险',
            'single_glass_broken':'玻璃单独破碎险',
			'natural_loss':'自然损失险',
			'new_add_equip':'新增加设备损失险',
			'scratch':'车身划痕损失险',
			'engine_water':'发动机涉水损失险',
			'while_repair':'修理期间费用补偿险',
			'cargo':'车上货物责任险',
			'mental_loss':'精神损害抚慰金责任险',
			'frachise':'不计免赔率险',
			'third_party_missing':'机动车损失保险无法找到第三方特约险',
			'assign_repair':'指定修理厂险',
			'insurance_company':'指定保险公司'


        }

class ImageForm(forms.ModelForm):
 	image = forms.ImageField(label='点此拍照')

 	class Meta:
 		model = Image
 		fields = ('image',)
