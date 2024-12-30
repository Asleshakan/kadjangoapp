# myproject/myapp/urls.py
# mydjango/myapp/urls.py

# mydjango/myapp/urls.py

from django.urls import path
from .views import my_view  # Import your view function

urlpatterns = [
    path('', my_view, name='my-view'),
    # Add other URL patterns for your app as needed
]


