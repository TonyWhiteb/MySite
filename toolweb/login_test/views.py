from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('INDEX')

def viewlogin(request):
    return HttpResponse('LOGIN')

def viewregister(request):
    return HttpResponse('REGISTER')    


