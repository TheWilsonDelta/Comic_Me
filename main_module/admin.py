from django.contrib import admin

from . import models


class ImageAdmin(admin.ModelAdmin):
    list_display = ("name", "user", "uploaded_at", "category")


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


class LanguageAdmin(admin.ModelAdmin):
    list_display = ("name",)


admin.site.register(models.Image, ImageAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Language, LanguageAdmin)
