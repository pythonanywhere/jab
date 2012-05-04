# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Post.posted'
        db.delete_column('main_post', 'posted')

        # Adding field 'Post.published'
        db.add_column('main_post', 'published',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 5, 4, 0, 0)),
                      keep_default=False)

    def backwards(self, orm):
        # Adding field 'Post.posted'
        db.add_column('main_post', 'posted',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2012, 5, 4, 0, 0), blank=True),
                      keep_default=False)

        # Deleting field 'Post.published'
        db.delete_column('main_post', 'published')

    models = {
        'main.post': {
            'Meta': {'object_name': 'Post'},
            'contents': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'published': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        }
    }

    complete_apps = ['main']