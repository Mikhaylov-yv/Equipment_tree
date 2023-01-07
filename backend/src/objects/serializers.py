from rest_framework import serializers
from objects.models import Objects, Object_types, Tree, Tree_types_connect

class ObjectsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Objects
        fields = ('id',
                  'title',
                  'description',
                  'type')

class Object_typesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Object_types
        fields = ('id',
                  'title',
                  'short_title')
                  