from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def nikki(request):
    return HttpResponse('This is shewage page')

def shewage(request):
    return render(request,'shewage.html')