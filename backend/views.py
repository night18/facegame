# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from random import randint
from django.template import loader
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
# Create your views here.
def index(request):
	fake_dir = ['nvidia','myfake']
	realface = ['00','01','02','03','04','05','06','07','08','09']
	nvidia = ['10','11','12','13','14','15','16','17','18','19']
	myfake = ['20','21','22','23','24','25','26','27','28','29']

	fake_idx = randint(0,1) #0 is nvidia, 1 is myfake
	if fake_idx == 0:
		fake_img_idx = nvidia[randint(0, len(nvidia)-1)]
	else:
		fake_img_idx = myfake[randint(0, len(myfake)-1)]

	real_img_idx = realface[randint(0, len(realface)-1)]

	real_url = 'https://s3.amazonaws.com/realfacehd/realface/000{}.png'.format(real_img_idx)
	fake_url = 'https://s3.amazonaws.com/realfacehd/{}/000{}.png'.format(fake_dir[fake_idx],fake_img_idx)

	# template = loader.get_template('index.html')
	print(real_url)
	print(fake_url)
	context = {
		'real_url': real_url,
		'real_img_idx': real_img_idx,
		'fake_url': fake_url,
		'fake_img_idx': fake_img_idx,
		'fake_dir_idx': fake_idx
	}

	return Response(context,status=HTTP_200_OK)