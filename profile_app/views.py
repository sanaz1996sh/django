from django.shortcuts import render,HttpResponse

#create your views here.
def info (request):
    return HttpResponse("<b><h2> اطلاعات مربوط به پروفایل من <h2><b>")
def sett(request):
    return HttpResponse("<b><h2>تنظیمات مربوط به پروفایل من<h2><b>")
