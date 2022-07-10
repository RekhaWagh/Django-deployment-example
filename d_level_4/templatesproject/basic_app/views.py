from django.shortcuts import render
from django.contrib import admin
from django.http import HttpResponse
# Create your views here.
def index(request):
    di={'text':"hello world",'num':100}
    return render(request,'basic_app/index.html',di)

def other(request):
    return render(request,'basic_app/other.html')

def relative(request):
    return render(request,'basic_app/relative_url_template.html')       