from django.db import models


# Create your models here.
# name, material, and manufacturerDate
class Cup(models.Model):
    name = models.CharField(max_length=200, default="")
    material = models.CharField(max_length=200, default="")
    manufacturerDate = models.DateField(default="")

    def __str__(self):
        return f'{self.name}'

#shows the name of the cups made rather than the default