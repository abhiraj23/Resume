
from django.contrib import admin
from django.urls import path, include

from core import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
    path("edu/", include("edu.urls")),
    path("serv/", include("serv.urls")),
    # path('', views.home, name='home')
]
