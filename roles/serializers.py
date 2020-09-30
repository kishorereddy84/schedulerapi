from rest_framework import serializers

from .models import role

class roleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = role
        fields = ('id', 'name', 'description','skill','certification')
