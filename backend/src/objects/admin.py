from django.contrib import admin

from .models import *

class Object_typesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'short_title')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'short_title')

class ObjectsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'type')
    list_display_links = ('id', 'title')
    search_fields = ('title',)

class Tree_types_connectAdmin(admin.ModelAdmin):
    list_display = ('id', 'short_title', 'title')
    list_display_links = ('id', 'short_title')
    search_fields = ('short_title', 'title')

class TreeAdmin(admin.ModelAdmin):
    list_display = ('id', 'parent', 'child', 'number', 'type')
    list_display_links = ('id', 'parent', 'child')
    search_fields = ('parent', 'child')
    list_editable = ('number',)





admin.site.register(Object_types, Object_typesAdmin)
admin.site.register(Objects, ObjectsAdmin)
admin.site.register(Tree_types_connect, Object_typesAdmin)
admin.site.register(Tree, TreeAdmin)