# from rest_framework import serializers
# from objects.models import *
# class ObjectsSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=200)
#     description = serializers.CharField(max_length=200)
#     type = serializers.CharField(source='type.title', max_length=70)
#     type_short_title = serializers.CharField(source='type.short_title', max_length=20)

# class POST_ObjectsSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=200)
#     description = serializers.CharField(max_length=200)
#     type_short_title = serializers.CharField(max_length=20)

# class Object_typesSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = StructurElements
#         fields = ('id',
#                   'title',
#                   'short_title')
                  