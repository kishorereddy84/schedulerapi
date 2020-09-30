from rest_framework import serializers

from .models import employee, employeeavailability


class employeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = employee
        fields = ('id', 'firstname', 'lastname', 'email', 'phone',
                  'address', 'address2', 'state', 'country', 'contracthours', 'location', 'department', 'role',
                  'skills', 'certifications', 'employeetype', 'hourlyrate')


class employeeAvailabiltySerializer(serializers.ModelSerializer):
    class Meta:
        model = employeeavailability
        fields = ('id', 'day', 'availability',
                  'startTime', 'endTime', 'employee', 'dayOfTheWeek')
