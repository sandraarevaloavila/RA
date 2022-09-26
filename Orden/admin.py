from django.contrib import admin
from .models import Compra, CompraItem


class CompraItemInline(admin.TabularInline):
    model = CompraItem
    raw_id_fields = ['producto']


@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ['id', 'usuario', 'direccion', 'lugar', 'telefono', 'fecha', 'total', ]
    list_filter = ['fecha']
    inlines = [CompraItemInline]


from django.contrib import admin

# Register your models here.
