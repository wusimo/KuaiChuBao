# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from KuaiChuBao.settings import BASE_DIR

from django.http import HttpResponse, HttpResponseRedirect

from .forms import ImageForm, PostForm, InsuranceForm
from django.forms import modelformset_factory

from .models import UserInfo,Image,Claim,Insurance


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
			return render(request, 'userRegister.html')
		elif request.session.get('type', False):
			request.session['type'] = request.GET.get('type')
			return render(request, 'userRegister.html')
		else:
			return render(request, '404.html')

	elif request.method == 'POST':
		if request.POST.get('name', False) and request.POST.get('national_id', False) and request.POST.get('phone', False):
			user, create = UserInfo.objects.get_or_create(
				national_id_number=request.POST.get('national_id'),
			)
			user.name = request.POST.get('name'),
			user.phone = request.POST.get('phone')
			user.save()
			request.session['step'] = 1
			request.session['user_id'] = user.id
			return HttpResponseRedirect('/claim/upload')


def choose_insurance(request,claim_id=None,step=None,step_name=None):

	if step_name == '保险信息采集':

		print '12345678'
		InsuranceFormSet = modelformset_factory(Insurance,
	 	                                    form=InsuranceForm, extra=1)

		if request.method=='POST':
			try:
				claim_id = request.claim_id
	 			claim = Claim.objects.filter(id=claim_id)[0]
	 		except:
	 			# TODO: need to add login here!!!
	 			claim = Claim(user=UserInfo.objects.all()[0])
	 			claim.save()
	 			claim_id = claim.id
	 		print "here"
	 		formset = InsuranceFormSet(request.POST, request.FILES,
	 		                       queryset=Insurance.objects.none())

	 		if  formset.is_valid(): #postForm.is_valid() and

	 			# add a new claim and link the posted form with claim
	 			#post_form = postForm.save(commit=False)
	 			#post_form.save()

	 			for form in formset.cleaned_data:
	 				# try:
	 				obligatory = form['obligatory']
	 				tax = form['tax']
	 				loss = form['loss']
	 				third_party = form['third_party']
	 				people_in_car = form['people_in_car']
	 				stolen_insurance = form['stolen_insurance']
	 				single_glass_broken  = form['single_glass_broken']
	 				natural_loss = form['natural_loss']
					new_add_equip = form['new_add_equip']
					scratch = form['scratch']
					engine_water = form['engine_water']
					while_repair = form['while_repair']
					cargo = form['cargo']
					mental_loss = form['mental_loss']
					franchise = form['frachise']
					third_party_missing = form['third_party_missing']
					assign_repair = form['assign_repair']
					insurance_company = form['insurance_company']

	 				insuranceform = Image(obligatory=obligatory,tax=tax,loss = loss,
	 					third_party = third_party, people_in_car = people_in_car,
	 					stolen_insurance = stolen_insurance, single_glass_broken = single_glass_broken,
	 					natural_loss = natural_loss, new_add_equip = new_add_equip,
	 					scratch = scratch, engine_water = engine_water, while_repair = while_repair,
	 					cargo = cargo, mental_loss = mental_loss, franchise = franchise,
	 					third_party_missing = third_party_missing,assign_repair= assign_repair,
	 					insurance_company = insurance_company,claim=claim)
	 				
	 				insuranceform.save()



			return render(request,'ChooseInsurance.html',{'claim_id':claim.id})

		else:
			
			formset = InsuranceFormSet(queryset=Insurance.objects.none())
			print '123456782983749823749'
			return render(request,'ChooseInsurance.html',{'claim_id':claim_id,
	 															'step':step,
	 															'step_name':'保险信息采集',
	 															'formset':formset})


def image_upload(request):

	print request.session.get('step_name', 'Shit')
	if request.session.get('step_name', False) and request.session.get('step_name', False)=='保险信息采集':
		

		print '123'
		InsuranceFormSet = modelformset_factory(Insurance,
	 	                                    form=InsuranceForm, extra=1)

		if request.method=='POST':
			try:
				claim_id = request.claim_id
	 			claim = Claim.objects.filter(id=claim_id)[0]
	 		except:
	 			# TODO: need to add login here!!!
	 			claim = Claim(user=UserInfo.objects.all()[0])
	 			claim.save()
	 			claim_id = claim.id
	 		print "herewocao"
	 		formset = InsuranceFormSet(request.POST, request.FILES,
	 		                       queryset=Insurance.objects.none())

	 		if  formset.is_valid(): #postForm.is_valid() and

	 			# add a new claim and link the posted form with claim
	 			#post_form = postForm.save(commit=False)
	 			#post_form.save()

	 			for form in formset.cleaned_data:
	 				# try:
	 				try:
	 					obligatory = form['obligatory']
	 				except:
	 					obligatory = False
	 				try:
	 					tax = form['tax']
	 				except:
	 					tax = False
	 				try:
	 					loss = form['loss']
	 				except:
	 					loss = False

	 				third_party = form['third_party']
	 				people_in_car = form['people_in_car']
	 				
	 				try:
	 					stolen_insurance = form['stolen_insurance']
	 				except:
	 					stolen_insurance = False
	 				try:
	 					single_glass_broken  = form['single_glass_broken']
	 				except:
	 					single_glass_broken = False
	 				try:
	 					natural_loss = form['natural_loss']
					except:
						natural_loss = False
					try:
						new_add_equip = form['new_add_equip']
					except:
						new_add_equip = False
					try:
						scratch = form['scratch']
					except:
						scratch = False
					try:
						engine_water = form['engine_water']
					except:
						engine_water = False
					try:
						while_repair = form['while_repair']
					except:
						while_repair = False
					try:
						cargo = form['cargo']
					except:
						cargo = False
					try:
						mental_loss = form['mental_loss']
					except:
						mental_loss = False
					try:
						franchise = form['frachise']
					except:
						franchise = False
					try:
						third_party_missing = form['third_party_missing']
					except:
						third_party_missing = False
					try:
						assign_repair = form['assign_repair']
					except:
						assign_repair = False	
					insurance_company = form['insurance_company']

	 				insuranceform = Insurance(obligatory=obligatory,tax=tax,loss = loss,
	 					third_party = third_party, people_in_car = people_in_car,
	 					stolen_insurance = stolen_insurance, single_glass_broken = single_glass_broken,
	 					natural_loss = natural_loss, new_add_equip = new_add_equip,
	 					scratch = scratch, engine_water = engine_water, while_repair = while_repair,
	 					cargo = cargo, mental_loss = mental_loss, frachise = franchise,
	 					third_party_missing = third_party_missing,assign_repair= assign_repair,
	 					insurance_company = insurance_company,claim=claim)
	 				
	 				insuranceform.save()



			#return render(request,'ChooseInsurance.html',{'claim_id':claim.id})

			del request.session['step_name']
			del request.session['step']
			return HttpResponseRedirect('/claim')

		else:
			
			#formset = InsuranceFormSet(queryset=Insurance.objects.none())
			#print '123456782983749823749'
			#return render(request,'ChooseInsurance.html',{'claim_id':claim_id,
	 		#													'step':step,
	 		#													'step_name':'保险信息采集',
	 		#														'formset':formset})
			del request.session['step_name']
			del request.session['step']
			return HttpResponseRedirect('/claim')
	
	type_step = {
		'danche' : ['站在事故车辆前45度角，10米处拍照。如下图：',
		            '站在事故车辆前45度角，5米处拍照。如下图：',
		            '站在事故车辆前45度角，1米处拍照。如下图：',
		            '站在事故车辆后45度角，10米处拍照。如下图：',
		            '站在事故车辆后45度角，5米处拍照。如下图：',
		            '站在事故车辆后45度角，1米处拍照。如下图：',
		            '在事故车辆前挡风玻璃处拍照车辆识别代号。如下图：',
		            '车辆移开后对准车辆受损部位和擦刮物体部位拍照。如下图：',
		            '人车合影，站在事故车辆前方或后方，拿手机对准自己和事故车辆拍照，必须照下事故车辆的号牌。如下图：',
		            '拿出行车证拍照。如下图：',
		            '拿出驾驶证拍照。如下图：',
		            '拿出被保险人身份证正面拍照。如下图：',
		            '拿出被保险人身份证反面拍照。如下图：',
		            '拿出被被保险人银行卡拍照。如下图：'
		            ],
		'guaca'  : ['站在事故车辆前45度角，10米处拍照。如下图：',
		            '站在事故车辆前45度角，5米处拍照。如下图：',
		            '站在事故车辆前45度角，1米处拍照。如下图：',
		            '站在事故车辆后45度角，10米处拍照。如下图：',
		            '站在事故车辆后45度角，5米处拍照。如下图：',
		            '站在事故车辆后45度角，1米处拍照。如下图：',
		            '在事故车辆前挡风玻璃处拍照车辆识别代号。如下图：',
		            '车辆移开后对准己方车辆受损部位和擦刮物体部位拍照。如下图：',
		            '车辆移开后对准对方车辆受损部位和擦刮物体部位拍照。如下图：',
		            '人车合影，站在事故车辆前方或后方，拿手机对准自己和事故车辆拍照，必须照下事故车辆的号牌。如下图：',
		            '拿出行车证拍照。如下图：',
		            '拿出驾驶证拍照。如下图：',
		            '拿出被保险人身份证拍照。如下图：',
		            '拿出被保险人身份证拍照。如下图：',
		            '拿出被被保险人银行卡拍照。如下图：'
		            ],
		'zhuiwei': ['站在事故车辆前45度角，10米处拍照。如下图：',
		            '站在事故车辆前45度角，5米处拍照。如下图：',
		            '站在事故车辆前45度角，1米处拍照。如下图：',
		            '站在事故车辆后45度角，10米处拍照。如下图：',
		            '站在事故车辆后45度角，5米处拍照。如下图：',
		            '站在事故车辆后45度角，1米处拍照。如下图：',
		            '在事故车辆前挡风玻璃处拍照车辆识别代号。如下图：',
		            '车辆移开后对准己方车辆受损部位和擦刮物体部位拍照。如下图：',
		            '车辆移开后对准对方车辆受损部位和擦刮物体部位拍照。如下图：',
		            '人车合影，站在事故车辆前方或后方，拿手机对准自己和事故车辆拍照，必须照下事故车辆的号牌。如下图：',
		            '拿出行车证拍照。如下图：',
		            '拿出驾驶证拍照。如下图：',
		            '拿出被保险人身份证拍照。如下图：',
		            '拿出被被保险人银行卡拍照。如下图：'
		            ],
	}

	if request.session.get('type', False) and request.session.get('step', False):
		type = request.session.get('type', False)
		step = request.session.get('step', False)
		

	ImageFormSet = modelformset_factory(Image,
 	                                    form=ImageForm, extra=1)

 	if request.method == 'POST':
 		try:
 			claim_id = request.session.claim_id
 			claim = Claim.objects.filter(id=claim_id)[0]
 		except:
 			# TODO: need to add login here!!!
 			claim = Claim(user=UserInfo.objects.all()[0])
 			claim.save()
 			#claim_id = claim.id
 		#postForm = PostForm(request.POST)
 		formset = ImageFormSet(request.POST, request.FILES,
 		                       queryset=Image.objects.none())

 		if  formset.is_valid(): #postForm.is_valid() and

 			# add a new claim and link the posted form with claim
 			#post_form = postForm.save(commit=False)
 			#post_form.save()

 			try:
	 			for form in formset.cleaned_data:
	 				# try:
	 				
	 				image = form['image']
	 				photo = Image(image=image,claim=claim)
	 				photo.save()
 			except:
 				pass
 			# messages.success(request,
 			#                 "Yeeew,check it out on the home page!")
			if step <len(type_step[type]):
				step = request.session.get('step', False)
				step_name = type_step[type][step - 1]
				request.session['step']=step+1
				step+=1
				print step

				img_url = 'img/' + type + '/' + str(step-1) + '.png'

			
 				return render(request, 'imageUpload.html', {'type'     : type,
		                                            'step'     : step,
		                                            'step_name': step_name,
		                                            'img_url'  : img_url,
		                                            #'postForm': postForm, 
		                                            'formset': formset,
		                                            'claim_id':claim.id})
 			else:

 				InsuranceFormSet = modelformset_factory(Insurance,
 	                                    form=InsuranceForm, extra=1)
 				
 				formset = InsuranceFormSet(queryset=Insurance.objects.none())

 				print '12345678'
 				request.session['step_name']='保险信息采集'
 				return render(request,'ChooseInsurance.html',{'claim_id':claim.id,'step':step,'step_name':'保险信息采集','formset':formset})
 		else:
 			print  formset.errors #postForm.errors,

 			return HttpResponseRedirect('/')


 		# render the next step
 		

 	else:
 		#postForm = PostForm()
 		formset = ImageFormSet(queryset=Image.objects.none())
 	
	
	

	if request.session.get('type', False) and request.session.get('step', False):
		type = request.session.get('type', False)
		step = request.session.get('step', False)
		if step >=len(type_step[type]):
			request.session['step']=1
			step = 1
		step_name = type_step[type][step - 1]
		img_url = 'img/' + type + '/' + str(step-1) + '.png'

		return render(request, 'imageUpload.html', {'type'     : type,
		                                            'step'     : step,
		                                            'step_name': step_name,
		                                            'img_url'  : img_url,
		                                            #'postForm': postForm, 
		                                            'formset': formset})


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
