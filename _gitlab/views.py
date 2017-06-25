# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets
from models import Project, Namespace
from serializers import ProjectSerializer, NamespaceSerializer
from filters import NamespaceFilter, ProjectFilter

# Create your views here.
class NamespaceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Namespace.objects.filter(_type='Group').order_by('-created_at')
    serializer_class = NamespaceSerializer
    filter_class = NamespaceFilter
    search_fields = ('name', 'path')


class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.all().order_by('-created_at')
    serializer_class = ProjectSerializer
    filter_class = ProjectFilter
    search_fields = ('name', 'path')
    
