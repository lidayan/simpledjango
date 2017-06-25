# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = 'users'

    def __unicode__(self):
        return self.username


class Namespace(models.Model):
    name = models.CharField(max_length=50)
    path = models.CharField(max_length=50)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    _type = models.CharField(max_length=20, db_column='type')
    owner = models.ForeignKey(User, null=True)

    class Meta:
        db_table = 'namespaces'

    def __unicode__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=50)
    path = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    creator = models.ForeignKey(User)
    namespace = models.ForeignKey(Namespace)

    class Meta:
        db_table = 'projects'

    def __unicode__(self):
        return self.name


class ProjectStatistic(models.Model):
    project = models.ForeignKey(Project)
    namespace = models.ForeignKey(Namespace)
    commit_count = models.IntegerField()
    repository_size = models.BigIntegerField()

    class Meta:
        db_table = 'project_statistics'

    def __unicode__(self):
        return "%s/%s" % (self.namespace.path, self.project.path)


class Member(models.Model):
    access_level = models.IntegerField()
    user = models.ForeignKey(User)
    _type = models.CharField(max_length=30)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    source_type = models.CharField(max_length=30)
    source_id = models.IntegerField()

    class Meta:
        db_table = 'members'

    def __unicode__(self):
        if self.source_type == 'Project':
            source = Project.objects.get(id=self.source_id)
        elif self.source_type == 'Namespace':
            source = Namespace.objects.get(id=self.source_id)
        else:
            return 'no-no'
        return "%s-%s" % (self.user.name, source.name)


class Branch(models.Model):
    name = models.CharField(max_length=100)
    project_id = models.IntegerField()
    protected = models.BooleanField()
    merged = models.BooleanField(default=False)

    def __unicode__(self):
        project = Project.objects.get(id=self.project_id)
        return '%s/%s-%s' % (project.namespace.path, project.path, self.self.name)


class Commit(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    title = models.CharField(max_length=200)
    message = models.TextField(default='')
    branch = models.ForeignKey(Branch)
    author = models.ForeignKey(User)
    created_at = models.DateTimeField()

    def __unicode__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField(default='', blank=True)
    commit = models.ForeignKey(Commit)

    def __unicode__(self):
        return self.name
