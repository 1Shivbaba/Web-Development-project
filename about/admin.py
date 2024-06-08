from django.contrib import admin
from about.models import About
# Register your models here.

class AboutAdmin(admin.ModelAdmin):
    list_display = ('about_title','about_desc', 'about_img')


admin.site.register(About,AboutAdmin)