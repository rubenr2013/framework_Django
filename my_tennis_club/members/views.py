from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
"""
def members(request):
    return HttpResponse("Hellow world!!")
"""
# Create your views here.
def members(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())