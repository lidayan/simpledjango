# -*- coding: utf-8 -*-
'''
设置 app.model 对应的数据
'''
class DatabaseAppsRouter(object):
    """
    A router to control all database operations on models for different
    databases.
 
    In case an app is not set in settings.DATABASE_APPS_MAPPING, the router
    will fallback to the `default` database.
 
    Settings example:
 
    DATABASE_APPS_MAPPING = {'app1': 'db1', 'app2': 'db2'}
    """

    DATABASE_MAPPING = {
        '_redmine.user': 'redmine',
        '_redmine.project': 'redmine',
        '_redmine.member': 'redmine',
        '_redmine.role': 'redmine',
        '_redmine.memberrole': 'redmine',
        '_redmine.tracker': 'redmine',
        '_redmine.issuestatus': 'redmine',
        '_redmine.issue': 'redmine',

        '_gitlab.user': 'gitlab',
        '_gitlab.namespace': 'gitlab',
        '_gitlab.project': 'gitlab',
        '_gitlab.member': 'gitlab',
        '_gitlab.projectstatistic': 'gitlab'
    }
 
    def db_for_read(self, model, **hints):
        """"Point all read operations to the specific database."""
        mapkey = '%s.%s' % (model._meta.app_label,model._meta.model_name)
        if mapkey in self.DATABASE_MAPPING:
            return self.DATABASE_MAPPING[mapkey]
        return None
 
    def db_for_write(self, model, **hints):
        """Point all write operations to the specific database."""
        mapkey = '%s.%s' % (model._meta.app_label,model._meta.model_name)
        if mapkey in self.DATABASE_MAPPING:
            return self.DATABASE_MAPPING[mapkey]
        return None
 
    def allow_relation(self, obj1, obj2, **hints):
        """Allow any relation between apps that use the same database."""
        mapkey1 = '%s.%s' % (obj1._meta.app_label, obj1._meta.model_name)
        mapkey2 = '%s.%s' % (obj2._meta.app_label, obj2._meta.model_name)
        db_obj1 = self.DATABASE_MAPPING.get(mapkey1)
        db_obj2 = self.DATABASE_MAPPING.get(mapkey2)
        if db_obj1 and db_obj2:
            return db_obj1 == db_obj2
        return None
 
    def allow_migrate(self, db, app_label, model_name, **kwargs):
        """Make sure that apps only appear in the related database."""
        mapkey = '%s.%s' % (app_label, model_name)
        if mapkey in self.DATABASE_MAPPING:
            return self.DATABASE_MAPPING.get(mapkey) == db
        return None
