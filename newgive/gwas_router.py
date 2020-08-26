# -*- coding: UTF-8 -*-
class GwasRouter:
    """
    A router to control all database operations on models in the app02 application.
    """
    gwas_app_labels = {'gwasdb'}


    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.gwas_app_labels:
            return 'gwas' 
        return None

 
    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.gwas_app_labels:
            return 'gwas' 
        return None
 
    def allow_relation(self, obj1, obj2, **hints):
        db_set = {'basic', 'gwas'}
        if obj1._state.db in db_set and obj2._state.db in db_set:
            return True
        return None
 
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        All non-auth models end up in this pool.
        """
        if app_label in self.gwas_app_labels:
            return db == 'gwas'
        return None
