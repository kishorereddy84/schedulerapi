from rest_framework import serializers

from .models import certifications

class certificationsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = certifications
        fields = ('id','name')