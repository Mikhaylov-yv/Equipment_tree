from django.db import models

class Object_types(models.Model):
    title = models.CharField(max_length=70, unique=True)


class Objects(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200,blank=False, default='')
    type = models.ForeignKey(Object_types, on_delete=models.CASCADE)

class Tree_types_connect(models.Model):
    title = models.CharField(max_length=70, unique=True)

class Tree(models.Model):
    parent = models.ForeignKey(Objects, related_name='parent_in_Objects',  on_delete=models.CASCADE)
    child = models.ForeignKey(Objects, related_name='child_in_Objects', on_delete=models.CASCADE)
    type = models.ForeignKey(Tree_types_connect, on_delete=models.CASCADE)
