# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    login = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    status = models.IntegerField()
    _type = models.CharField(max_length=10, db_column='type')

    class Meta:
        db_table = 'users'

    def __unicode__(self):
        return self.login


class Project(models.Model):
    identifier = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    description = models.TextField()
    parent_id = models.IntegerField()
    status = models.IntegerField()
    created_at = models.DateTimeField(db_column='created_on')
    updated_at = models.DateTimeField(db_column='updated_on')

    class Meta:
        db_table = 'projects'

    def __unicode__(self):
        return self.name


class Member(models.Model):
    user = models.ForeignKey(User)
    project = models.ForeignKey(Project)
    created_at = models.DateTimeField(db_column='created_on')

    class Meta:
        db_table = 'members'

    def __unicode__(self):
        return '%s-%s' % (self.project.name, self.user.login)


class Role(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'roles'

    def __unicode__(self):
        return self.name


class MemberRole(models.Model):
    member = models.ForeignKey(Member)
    role = models.ForeignKey(Role)

    class Meta:
        db_table = 'member_roles'

    def __unicode__(self):
        return '%s-%s' % (self.role.name, self.member)


class Tracker(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'trackers'

    def __unicode__(self):
        return self.name


class IssueStatus(models.Model):
    name = models.CharField(max_length=50)
    is_closed = models.BooleanField()

    class Meta:
        db_table = 'issue_statuses'

    def __unicode__(self):
        return self.name


class Issue(models.Model):
    project = models.ForeignKey(Project)
    subject = models.CharField(max_length=200)
    description = models.TextField()
    assigned_to = models.ForeignKey(User, related_name='assigned_to')
    author = models.ForeignKey(User, related_name='author')
    parent_id = models.IntegerField()
    status = models.ForeignKey(IssueStatus)

    created_at = models.DateTimeField(db_column='created_on')
    updated_at = models.DateTimeField(db_column='updated_on')
    closed_at = models.DateTimeField(db_column='closed_on')

    class Meta:
        db_table = 'issues'

    def __unicode__(self):
        return self.subject

