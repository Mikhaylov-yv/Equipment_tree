from django.contrib import admin

from .models import *

class StructurElementsTypesAdmin(admin.ModelAdmin):
    list_display = ('id', 'short_name', 'name')
    list_display_links = ('id',)
    search_fields = ('short_name', 'name')

class StructurElementsAdmin(admin.ModelAdmin):
    list_display = ('id', 'draw_num', 'name', 'description', 'type')
    list_display_links = ('id',)

class TypeConTreeStructurAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)

class TreeStructurAdmin(admin.ModelAdmin):
    list_display = ('id', 'parent','child', 'type', 'number')
    list_display_links = ('id',)
    list_filter = ('parent', 'type')

class InstancesElementAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)

class TreeElemrntsAdmin(admin.ModelAdmin):
    list_display = ('id', 'element', 'parent', 'type')
    list_display_links = ('id',)


admin.site.register(StructurElementsTypes, StructurElementsTypesAdmin)
admin.site.register(StructurElements, StructurElementsAdmin)
admin.site.register(TypeConTreeStructur, TypeConTreeStructurAdmin)
admin.site.register(TreeStructur, TreeStructurAdmin)
admin.site.register(InstancesElement, InstancesElementAdmin)
admin.site.register(TreeElemrnts, TreeElemrntsAdmin)