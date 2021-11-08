
from django.contrib import admin
from django.urls import path

from myapp.views import show

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', show),

]
