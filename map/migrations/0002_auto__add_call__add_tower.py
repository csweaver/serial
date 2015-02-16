# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Call'
        db.create_table(u'map_call', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
            ('time', self.gf('django.db.models.fields.DateTimeField')()),
            ('duration', self.gf('django.db.models.fields.IntegerField')()),
            ('tower', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['map.Tower'])),
        ))
        db.send_create_signal(u'map', ['Call'])

        # Adding model 'Tower'
        db.create_table(u'map_tower', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
            ('x', self.gf('django.db.models.fields.IntegerField')()),
            ('y', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'map', ['Tower'])


    def backwards(self, orm):
        # Deleting model 'Call'
        db.delete_table(u'map_call')

        # Deleting model 'Tower'
        db.delete_table(u'map_tower')


    models = {
        u'map.call': {
            'Meta': {'object_name': 'Call'},
            'duration': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'time': ('django.db.models.fields.DateTimeField', [], {}),
            'tower': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['map.Tower']"})
        },
        u'map.tower': {
            'Meta': {'object_name': 'Tower'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'x': ('django.db.models.fields.IntegerField', [], {}),
            'y': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['map']