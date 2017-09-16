from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.landing, name='landing'),
    url(r'^user$', views.user_register, name='user_register'),
    url(r'^upload', views.image_upload, name='image_upload'),
    url(r'^company', views.insurance_company, name='insurance_company'),
    url(r'^choose',views.choose_insurance,name='choose_insurance'),
   
]