# -*- coding: utf-8 -*-
from django import forms
from .models import  Image #Post,


class PostForm(forms.ModelForm):
 	title = forms.CharField(max_length=128, label="Name")

 	# body = forms.CharField(max_length=245, label="Item Description.")
 	class Meta:
 		#model = Post
 		fields = ('title',)


class ImageForm(forms.ModelForm):
 	image = forms.ImageField(label='点此拍照')

 	class Meta:
 		model = Image
 		fields = ('image',)
