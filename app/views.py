from django.shortcuts import render,HttpResponse

# Create your views here.


def regest(req):

    print(req.GET)
    print(req.POST)
    print(req.FILES)

    return HttpResponse("注册成功")

def index(req):

    return