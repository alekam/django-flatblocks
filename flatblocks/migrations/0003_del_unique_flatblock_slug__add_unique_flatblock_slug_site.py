# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Removing unique constraint on 'FlatBlock', fields ['slug']
        db.delete_unique('flatblocks_flatblock', ['slug'])

        # Adding unique constraint on 'FlatBlock', fields ['slug', 'site']
        db.create_unique('flatblocks_flatblock', ['slug', 'site_id'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'FlatBlock', fields ['slug', 'site']
        db.delete_unique('flatblocks_flatblock', ['slug', 'site_id'])

        # Adding unique constraint on 'FlatBlock', fields ['slug']
        db.create_unique('flatblocks_flatblock', ['slug'])


    models = {
        'flatblocks.flatblock': {
            'Meta': {'unique_together': "(('slug', 'site'),)", 'object_name': 'FlatBlock'},
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'header': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': "orm['sites.Site']", 'blank': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['flatblocks']
