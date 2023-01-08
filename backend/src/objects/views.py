from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view

import logging
logger = logging.getLogger(__name__)

from objects.models import Objects, Object_types, Tree, Tree_types_connect
from objects.serializers import ObjectsSerializer, Object_typesSerializer 


# Создание типа объекта


# Создание объекта
@api_view(['GET', 'POST'])
def objects_list(request):
    if request.method == 'GET':
        objects = Objects.objects.all()
        title = request.data.get('title')
        logger.warning(title)
        if title is not None:
            objects = objects.filter(title__icontains=title)
        objects_serializer = ObjectsSerializer(objects, many=True)
        return JsonResponse(objects_serializer.data,  safe=False)

    elif request.method == 'POST':
        object_data = JSONParser().parse(request)
        objects_serializer = ObjectsSerializer(data=object_data)
        logger.warning('Создание объекта')
        logger.warning(object_data)
        if objects_serializer.is_valid():
            objects_serializer.save()
            return JsonResponse(objects_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(objects_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'DELETE'])
def objects_types(request):
    if request.method == 'GET':
        types = Object_types.objects.all()
        title = request.GET.get('title', None)
        if title is not None:
            types = types.filter(title__icontains=title)
        types_serialize = Object_typesSerializer(types, many=True)
        return JsonResponse(types_serialize.data, safe=False)

    elif request.method == 'POST':
        type_data = JSONParser().parse(request)
        types_serialize = Object_typesSerializer(data=type_data)
        if types_serialize.is_valid():
            types_serialize.save()
            return JsonResponse(types_serialize.data, status=status.HTTP_201_CREATED)
        return JsonResponse(types_serialize.errors, status=status.HTTP_400_BAD_REQUEST)            

    elif request.method == 'DELETE':
        pass
