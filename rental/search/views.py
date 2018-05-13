from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView
import requests
import json
from .models import *
from datetime import datetime,timedelta
from django.db.models import Q
from django.utils.decorators import method_decorator
import csv
import base64
from passlib.hash import django_pbkdf2_sha256 as handler
# from post_office import mail
# from post_office.models import EmailTemplate
from random import randint
from django.conf import settings
import pytz
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, HttpResponseRedirect, render_to_response
from django.contrib import messages
from django.contrib.gis import geoip
from django.contrib.gis.geoip import GeoIP
# from login.models import *
utc=pytz.UTC


					# ADMIN



class HomePage(TemplateView):
	template_name = "dashboard.html"


	def get_context_data(self, *args, **kwargs):
		context = super(HomePage, self).get_context_data()
		self.request.environ['REMOTE_ADDR']
		if  self.request.environ['REMOTE_ADDR'] == '127.0.0.1':
			context['ip']='157.39.138.172'
		else:
			context['ip']=self.request.environ['REMOTE_ADDR']
		g = GeoIP()
		location_data = g.city(context['ip'])
		# city = g.city('106.192.73.120')
		context['city']= location_data['city']
		context['country']= location_data['country_name']
		
		return context
	
	def post(self,request):
		print (request.POST)
		response={}
		email_id=request.POST.get('email')
		input_password=request.POST.get('passw')
		
		print ('\n')
		try:
			credentials=MainAdminCredentials.objects.get(email=email_id)
		except:
			print ('in except')
			response['email_error']='Email Does Not Exists'
			return HttpResponse(json.dumps(response))
		if credentials:
			database_password=credentials.password
			passw_verify=handler.verify(input_password,database_password)
			
			if passw_verify:
				print ('right')
				response['password_right']='Right Password'
				return HttpResponse(json.dumps(response))
			else:
				print ('wrong')
				response['password_error']='Wrong Password'
				return HttpResponse(json.dumps(response))

