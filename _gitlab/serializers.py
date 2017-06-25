# coding: utf8

from rest_framework import serializers
from models import Project, Namespace


class NamespaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Namespace
        fields = '__all__'

 
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
