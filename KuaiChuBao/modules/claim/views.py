# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from KuaiChuBao.settings import BASE_DIR

# from django.http import HttpResponse, HttpResponseRedirect

# from .forms import ImageForm, PostForm
# from django.forms import modelformset_factory


def landing(request):
	# formset = ImageFormSet(queryset=Images.objects.none())

	print BASE_DIR
	return render(request, 'landing.html')

#
# def post_picture(request):
# 	ImageFormSet = modelformset_factory(Images,
# 	                                    form=ImageForm, extra=3)
#
# 	if request.method == 'POST':
#
# 		postForm = PostForm(request.POST)
# 		formset = ImageFormSet(request.POST, request.FILES,
# 		                       queryset=Images.objects.none())
#
# 		if postForm.is_valid() and formset.is_valid():
#
# 			# add a new claim and link the posted form with claim
# 			post_form = postForm.save(commit=False)
# 			post_form.save()
#
# 			for form in formset.cleaned_data:
# 				# try:
# 				image = form['image']
# 				photo = Images(image=image)
# 				photo.save()
# 			# except:
# 			#    pass
# 			# messages.success(request,
# 			#                 "Yeeew,check it out on the home page!")
# 			return HttpResponseRedirect("/")
# 		else:
# 			print postForm.errors, formset.errors
# 	else:
# 		postForm = PostForm()
# 		formset = ImageFormSet(queryset=Images.objects.none())
# 	return render(request, 'index.html', {'postForm': postForm, 'formset': formset})
