from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('agregar_producto/<int:producto_id>', views.agregar_producto, name='agregar_producto'),
    path('eliminar_producto/<int:producto_id>', views.eliminar_producto, name='eliminar_producto'),
    path('restar_producto/<int:producto_id>', views.restar_producto, name='restar_producto'),
    path('limpiar_orden/', views.limpiar_orden, name='limpiar_orden'),
    path('procesar_pedido',views.procesar_pedido, name="procesar_pedido"),
]

urlpatterns += static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)