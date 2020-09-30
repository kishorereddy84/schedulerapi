from django.db import models

# Create your models here.


class department(models.Model):
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=180, null=True, blank=True)
    role = models.CharField(max_length=60, null=True, blank=True)

    def __str__(self):
        return self.name


class departmenttimings(models.Model):
    day = models.CharField(max_length=60)
    availability = models.BooleanField(blank=False, default=False)
    startTime = models.TimeField()
    endTime = models.TimeField()
    department = models.ForeignKey(
        department, on_delete=models.CASCADE, parent_link=True)
    dayOfTheWeek = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name
