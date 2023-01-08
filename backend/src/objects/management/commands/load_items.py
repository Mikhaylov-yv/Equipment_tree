import random

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.db.models import Q

from objects.models import Object_types, Objects

class Command(BaseCommand):
    def handle(self, *args, **options):
        Object_types.objects.all().delete()
        Objects.objects.all().delete()

        # Создание типов объектов
        objects_types = [
            Object_types(
                title=f"Название типа {index}", 
                short_title=f"Тип{index}"
                ) for index in range(1, 3)]
        Object_types.objects.bulk_create(objects_types)

        objects = []

        for counter, objects_type in enumerate(Object_types.objects.all()):
            for i in range(10):
                objects.append(Objects(
                    title=f"Объект №{counter}{i}", 
                    description=f"Описание объекта №{counter}{i}", 
                    type=objects_type)
                    )
        Objects.objects.bulk_create(objects)