from django.contrib import admin
from.models import Exceldata
from import_export.admin import ImportExportActionModelAdmin
# Register your models here.
@admin.register(Exceldata)
class AdminView(ImportExportActionModelAdmin):

    class Meta:
        model=Exceldata

from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Profile)