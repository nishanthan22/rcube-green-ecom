from django.contrib import admin
from .models import GreenInnovation, EcoProducts, SustainableLiving

# Register your models here.

class GreenInnovationAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(GreenInnovation, GreenInnovationAdmin)

class EcoProductsAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(EcoProducts, EcoProductsAdmin)

class SustainableLivingAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(SustainableLiving, SustainableLivingAdmin)
