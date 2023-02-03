from django.db import models

class StructurElementsTypes(models.Model):
    short_name = models.CharField(max_length=30, unique=True, verbose_name='Краткое наименование')
    name = models.CharField(max_length=70, blank=True, default='')

    def __str__(self):
        return self.short_name
    
    class Meta:
        verbose_name = 'Типы элементов конструкции'
        verbose_name_plural = verbose_name


class StructurElements(models.Model):
    draw_num = models.CharField(max_length=50, blank=True, default='')
    name = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=200,blank=True, default='')
    type = models.ForeignKey(
        StructurElementsTypes, on_delete=models.CASCADE,
         related_name='object_type')

    def __str__(self):
        return f"{self.id} {self.draw_num} {self.name}"
    class Meta:
        verbose_name = 'Элементы конструкции'
        verbose_name_plural = verbose_name

class TypeConTreeStructur(models.Model):
    short_name = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=70, blank=True, default='')
    
    def __str__(self):
        return self.short_name
    class Meta:
        verbose_name = 'Типы связей в дереве'
        verbose_name_plural = verbose_name

class TreeStructur(models.Model):
    parent = models.ForeignKey(StructurElements, related_name='parent_in_Objects',  on_delete=models.CASCADE)
    child = models.ForeignKey(StructurElements, related_name='child_in_Objects', on_delete=models.CASCADE)
    type = models.ForeignKey(TypeConTreeStructur, on_delete=models.CASCADE)
    number = models.IntegerField(default=1)

    def __str__(self):
        return self.parent.name

    class Meta:
        verbose_name = 'Конструктивное дерево'
        verbose_name_plural = verbose_name

class InstancesElement(models.Model):
    structur_element = models.ForeignKey(StructurElements, on_delete=models.CASCADE)
    serial_number = models.CharField(max_length=40, )
    kks = models.CharField(max_length=40,  blank=True, default='')

    def __str__(self):
        return self.structur_element.name
    class Meta:
        verbose_name = 'Серийные номера элементов'
        verbose_name_plural = verbose_name

class TreeElemrnts(models.Model):
    element = models.ForeignKey(InstancesElement, related_name='parent', on_delete=models.CASCADE)
    parent = models.ForeignKey(
        InstancesElement, related_name='child', default='', blank=True,
         null=True, on_delete=models.CASCADE)
    type = models.ForeignKey(TypeConTreeStructur, on_delete=models.CASCADE)
   
    def __str__(self):
        return self.element.structur_element.name
    class Meta:
        verbose_name = 'Дерево оборудования'
        verbose_name_plural = verbose_name