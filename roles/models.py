from django.db import models

# Create your models here.
class role(models.Model):
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=180,null=True,blank=True)
    skill = models.CharField(max_length=60,null=True,blank=True)
    certification = models.CharField(max_length=60,null=True,blank=True)

def __str__(self):
        return self.name