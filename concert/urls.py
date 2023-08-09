from django.contrib import admin
from django.urls import path
from profile_app.views import*
from concert_app.views import*

urlpatterns = [
    path('admin/', admin.site.urls),
    path('info/',info),
    path('sett/',sett),
    path('home/',home),
    path('news/',news),
    path('about/',about)

    ]


