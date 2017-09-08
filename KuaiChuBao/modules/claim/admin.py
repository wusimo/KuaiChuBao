# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
# -*- coding: utf-8 -*-
from .models import Claim,Post,Images,InsuranceCompany

admin.site.register(Claim)
admin.site.register(Post)
admin.site.register(Images)