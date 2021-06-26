from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User, auth

# Create your views here.

def index(request):
	a1 = Customer.objects.all()
	context = { 'a1' : a1 }
	return render (request, 'index.html', context)


def addorder(request):
	return render (request, 'addorder.html')
