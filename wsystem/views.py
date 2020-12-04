from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request,'wsystem/index.html')



def signin(request):
    print(request.POST)
    print(request.POST['inputEmail'])
    print(request.POST['inputPassword'])
    return render(request,'wsystem/index.html')