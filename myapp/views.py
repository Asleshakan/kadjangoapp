# myproject/myapp/views.py
# mydjango/myapp/views.py

from django.http import HttpResponse

def my_view(request):
    return HttpResponse("Hi, this is Django app")
