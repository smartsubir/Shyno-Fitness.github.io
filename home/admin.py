from django.contrib import admin
from home.models import Feedback
from import_export.admin import ImportExportModelAdmin # this is use for importing and exporting data from django admoin pannel

class showFields(ImportExportModelAdmin,admin.ModelAdmin): # here this additional class importexport is inherited because of import exporting
    list_display=('id','name','mid','phone','remark','date','QualityofEquipements','MaintenanceofEquipements','TrainersBehavior','QualityofPersonalTraining','NutritionistAdvisor','GymMusicSystem','GymEnvironment','HealthCalculator')

admin.site.register(Feedback,showFields)


