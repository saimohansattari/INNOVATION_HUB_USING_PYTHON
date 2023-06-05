from django.contrib import admin
from .models import Project

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    class meta:
        model = Project
    list_display = ['project_title','branch','year']    

admin.site.register(Project, ProjectAdmin)