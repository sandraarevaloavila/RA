from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('registro', views.form, name="registro"),
    path('productos', views.productos, name='productos'),
    path('contactenos', views.contactenos, name='contactenos')
]
urlpatterns += static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)