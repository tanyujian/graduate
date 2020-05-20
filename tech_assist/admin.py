from django.contrib import admin
from . models import TechFile,TechWork,CourseGrate
# Register your models here.

class TeachFileAdmin(admin.ModelAdmin):
    list_display = ["id","desc","video"]
class TechWorkAdmin(admin.ModelAdmin):
    list_display = ["id","user","course"]

admin.site.register(TechFile,TeachFileAdmin)
admin.site.register(TechWork,TechWorkAdmin)
admin.site.register(CourseGrate)
