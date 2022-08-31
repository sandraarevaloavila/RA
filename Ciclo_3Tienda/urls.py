from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('productos', views.productos, name="productos"),
    path('contactenos', views.contactenos, name="contactenos"),
]
