from django.contrib import admin
from django.urls import path, include
from fees.views import * 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('fees.urls'))
]
