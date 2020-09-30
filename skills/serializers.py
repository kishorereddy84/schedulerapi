from rest_framework import serializers

from .models import skills

class skillsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = skills
        fields = ('id','name')