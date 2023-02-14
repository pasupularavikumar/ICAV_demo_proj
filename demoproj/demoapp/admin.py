from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.

# admin.site.register(Book)

class bookAdmin(ImportExportModelAdmin, admin.ModelAdmin):
   ... 
admin.site.register(Book,bookAdmin)

from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass