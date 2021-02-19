from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('datamining_spa.urls')),
    path('admin/', admin.site.urls),
]