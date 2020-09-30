from rest_framework import serializers

from .models import location, locationtimings


class locationSerializer(serializers.ModelSerializer):
    class Meta:
        model = location
        fields = ('id', 'locid', 'locname', 'department', 'address1',
                  'address2', 'suburb', 'state', 'country', 'phone')


class locationtimingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = locationtimings
        fields = ('id', 'day', 'availability',
                  'startTime', 'endTime', 'location', 'dayOfTheWeek')
