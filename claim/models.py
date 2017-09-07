# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.template.defaultfilters import slugify

# Create your models here.

class Claim(models.Model):
	insuranceCompany = models.CharField(max_length = 50,null = True)
	# Information from page 1
	#车主身份证
	#identityCardFace = models.ImageField(upload_to='uploads/%Y/%m/%d/')
	#identityCardBottom = models.ImageField(upload_to='uploads/%Y/%m/%d/')
	#驾照
	#driverLicenseFace = models.ImageField(upload_to='uploads/%Y/%m/%d/')
	#driverLicenseBottom = models.ImageField(upload_to='uploads/%Y/%m/%d/')
	#商业保险
	#commercialInsurance = models.ImageField(upload_to='uploads/%Y/%m/%d/')
	#交强保险
	#obligatoryInsurance = models.ImageField(upload_to='uploads/%Y/%m/%d/')
	#被保险人身份证
	#insuredIdentityFace = models.ImageField(upload_to='uploads/%Y/%m/%d/')
	#insuredIdentityBottom = models.ImageField(upload_to='uploads/%Y/%m/%d/')



def get_image_filename(instance, filename):
    title = instance.claim
    slug = slugify(title)
    return "post_images/%s-%s" % (slug, filename)  

class Post(models.Model):
    claim = models.ForeignKey(Claim,null=True)
    title = models.CharField(max_length=128)
    #body = models.CharField(max_length=400)

class Images(models.Model):
    claim = models.ForeignKey(Claim,null = True)
    image = models.ImageField(upload_to=get_image_filename,
                              verbose_name='image', )

class InsuranceCompany(models.Model):
	name = models.CharField(max_length = 100)
	phoneNumber = models.CharField(max_length = 20, blank = True)

