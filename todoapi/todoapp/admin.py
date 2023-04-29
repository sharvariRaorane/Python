from django.contrib import admin
from .models import TODO
from import_export.admin import ImportExportModelAdmin
# Register your models here.
@admin.register(TODO)
class todo(ImportExportModelAdmin):
    pass