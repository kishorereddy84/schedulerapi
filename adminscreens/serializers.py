from rest_framework import serializers

from .models import emprequired


class emprequiredserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = emprequired
        fields = ('id', 'time', 'requiredemp')
