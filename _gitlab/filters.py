# coding: utf8

from django_filters import rest_framework as filters
from models import Namespace, Project

class NamespaceFilter(filters.FilterSet):
    class Meta:
        model = Namespace
        fields = ['id', 'name','path']

class ProjectFilter(filters.FilterSet):
    class Meta:
        model = Project
        fields = ['id', 'name','path']
