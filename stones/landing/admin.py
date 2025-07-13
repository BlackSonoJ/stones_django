from django.contrib import admin

from .models import Header, Service, Material


@admin.register(Header)
class HeaderAdmin(admin.ModelAdmin):
    list_display = ["id", "line1", "subline"]


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "subtitle", "text", "image"]


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "image"]
