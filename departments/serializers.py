from rest_framework import serializers

from .models import department, departmenttimings


class departmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = department
        fields = ('id', 'name', 'description', 'role')


class departmenttimingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = departmenttimings
        fields = ('id', 'day', 'availability',
                  'startTime', 'endTime', 'department', 'dayOfTheWeek')
