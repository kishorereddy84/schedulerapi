from django.db import models

# Create your models here.


class location(models.Model):
    locid = models.IntegerField()
    locname = models.CharField(max_length=60)
    department = models.CharField(max_length=60, null=True, blank=True)
    address1 = models.CharField(max_length=300)
    address2 = models.CharField(max_length=300)
    suburb = models.CharField(max_length=300)
    state = models.CharField(max_length=300)
    country = models.CharField(max_length=300)
    phone = models.IntegerField()

    def __str__(self):
        return self.locname


class locationtimings(models.Model):
    day = models.CharField(max_length=60)
    availability = models.BooleanField(blank=False, default=False)
    startTime = models.TimeField()
    endTime = models.TimeField()
    location = models.ForeignKey(
        location, on_delete=models.CASCADE, parent_link=True)
    dayOfTheWeek = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name
