from django.urls import re_path
from objects import views

urlpatterns = [
    re_path(r'^api/objects$', views.objects_list),
    re_path(r'^api/objects/types$', views.objects_types),
]
