from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<b><h1>سلام.خوش امدید<h1><b>")
def news(request):
    return HttpResponse("<h1> :خبرها<h1>"  "<b><h6>علیرضا قربانی رکوردشکن برگزاری کنسرت در چهار ماه اخیر است.   با نگاهی به وضعیت کنسرت‌ها در چهار ماهه ابتدایی سال و پیش از شروع محرم به این نتیجه رسیدیم که بزرگترین برگزار کننده کنسرت که رکورد شکن هم بوده، علیرضا قربانی است<h6><b>" )
def about(request):
    return HttpResponse("<u><h1>ما در تلاشیم که بهترین خدمات فروش بلیط کنسرت را ارائه دهیم<h1><u>")
