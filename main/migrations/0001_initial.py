# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Post'
        db.create_table('main_post', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('posted', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('contents', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('main', ['Post'])

    def backwards(self, orm):
        # Deleting model 'Post'
        db.delete_table('main_post')

    models = {
        'main.post': {
            'Meta': {'object_name': 'Post'},
            'contents': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'posted': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        }
    }

    complete_apps = ['main']