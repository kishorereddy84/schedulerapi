from django.db import models

# Create your models here.


class employee(models.Model):

    EMPLOYEE_TYPES = [('FT', 'Full Time'),
                      ('PT', 'Part Time'),
                      ('C', 'Casual')
                      ]

    firstname = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)
    email = models.CharField(max_length=60, default="k@k.com", null=True)
    phone = models.IntegerField(null=True)
    address = models.TextField(null=True)
    address2 = models.TextField(null=True)
    state = models.CharField(max_length=60, null=True)
    city = models.CharField(max_length=60, null=True)
    zip = models.CharField(max_length=60, null=True)
    country = models.CharField(max_length=60, null=True)
    contracthours = models.IntegerField(null=True)
    hourlyrate = models.DecimalField(null=True, max_digits=5, decimal_places=2)
    location = models.CharField(max_length=60, null=True, blank=True)
    department = models.CharField(max_length=60, null=True, blank=True)
    role = models.CharField(max_length=60, null=True, blank=True)
    skills = models.CharField(max_length=60, null=True, blank=True)
    certifications = models.CharField(max_length=60, null=True, blank=True)
    employeetype = models.CharField(
        choices=EMPLOYEE_TYPES, max_length=60, null=True)

    def __str__(self):
        return self.firstname


class employeeavailability(models.Model):
    day = models.CharField(max_length=60)
    availability = models.BooleanField(blank=False, default=False)
    startTime = models.TimeField()
    endTime = models.TimeField()
    employee = models.ForeignKey(
        employee, on_delete=models.CASCADE, parent_link=True)
    dayOfTheWeek = models.IntegerField(blank=True, null=True)
