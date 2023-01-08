from django.db import models

class Object_types(models.Model):
    short_title = models.CharField(max_length=20, unique=True, default='')
    title = models.CharField(max_length=70, unique=True, default=short_title)

    def __str__(self):
        return '%d: %s' % (self.short_title, self.title)


class Objects(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200,blank=False, default='')
    type = models.ForeignKey(Object_types, on_delete=models.CASCADE, related_name='object_type')

    def __str__(self):
        return f"{self.id}, {self.title}, {self.description}, {self.type}"

class Tree_types_connect(models.Model):
    short_title = models.CharField(max_length=20, unique=True, default='')
    title = models.CharField(max_length=70, unique=True, default=short_title)

class Tree(models.Model):
    parent = models.ForeignKey(Objects, related_name='parent_in_Objects',  on_delete=models.CASCADE)
    child = models.ForeignKey(Objects, related_name='child_in_Objects', on_delete=models.CASCADE)
    type = models.ForeignKey(Tree_types_connect, on_delete=models.CASCADE)
