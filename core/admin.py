from django.contrib import admin
from .models import Project
from django.utils.html import format_html


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('company', 'address', 'text', 'photo1_thumbnail', 'photo2_thumbnail', 'photo3_thumbnail')
    search_fields = ('company', 'text')
    list_filter = ('company',)


    def photo1_thumbnail(self, obj):
        if obj.photo1:
            return format_html('<img src="{}" width="50" height="50" />', obj.photo1.url)
        return "Нет изображения"

    photo1_thumbnail.short_description = 'Фото 1'

    def photo2_thumbnail(self, obj):
        if obj.photo2:
            return format_html('<img src="{}" width="50" height="50" />', obj.photo2.url)
        return "Нет изображения"

    photo2_thumbnail.short_description = 'Фото 2'

    def photo3_thumbnail(self, obj):
        if obj.photo3:
            return format_html('<img src="{}" width="50" height="50" />', obj.photo3.url)
        return "Нет изображения"

    photo3_thumbnail.short_description = 'Фото 3'


admin.site.register(Project, ProjectAdmin)
