# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from KuaiChuBao.settings import BASE_DIR

from django.http import HttpResponse, HttpResponseRedirect

# from .forms import ImageForm, PostForm
# from django.forms import modelformset_factory

from .models import UserInfo


def landing(request):
	# formset = ImageFormSet(queryset=Images.objects.none())
	if request.session.get('type', False) and request.session.get('step', False):
		return HttpResponseRedirect('/claim/upload')
	elif request.session.get('type', False):
		return HttpResponseRedirect('/claim/user')
	else:
		return render(request, 'landing.html')


def user_register(request):
	if request.method == 'GET':
		if request.GET.get('type', False):
			request.session['type'] = request.GET.get('type')
			return render(request, 'userRegster.html')
		elif request.session.get('type', False):
			request.session['type'] = request.GET.get('type')
			return render(request, 'userRegster.html')
		else:
			return render(request, '404.html')
	elif request.method == 'POST':
		if request.GET.get('name', False) and request.GET.get('national_id', False) and request.GET.get('phone', False):
			user = UserInfo.objects.get_or_create(
				national_id_number=request.GET.get('national_id', False),
			)
			user.name = request.GET.get('name')
			user.phone = request.GET.get('phone')
			user.save()
			request.session['step'] = 0
			return HttpResponseRedirect('/claim/upload')


def image_upload(request):
	if request.session.get('type', False) and request.session.get('step', False):
		pass


def insurance_company(request):
	return render(request, 'insuranceCompany.html')

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
