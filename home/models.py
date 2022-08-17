from django.db import models
from sqlalchemy import true

class Feedback(models.Model):
    name = models.CharField(max_length=30,null=true)
    mid = models.CharField(max_length=10,null=true)
    phone = models.CharField(max_length=10,null=true)
    remark = models.TextField(null=true)
    date = models.DateField()
    QualityofEquipements=models.CharField(max_length=1,null=true)
    MaintenanceofEquipements=models.CharField(max_length=1,null=true)
    TrainersBehavior=models.CharField(max_length=1,null=true)
    QualityofPersonalTraining=models.CharField(max_length=1,null=true)
    NutritionistAdvisor=models.CharField(max_length=1,null=true)
    GymMusicSystem=models.CharField(max_length=1,null=true)
    GymEnvironment=models.CharField(max_length=1,null=true)
    HealthCalculator=models.CharField(max_length=1,null=true)

    def __str__(self):
        return self.name

# Create your models here.
