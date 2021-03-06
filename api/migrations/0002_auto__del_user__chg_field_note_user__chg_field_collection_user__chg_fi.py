# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'User'
        db.delete_table(u'api_user')


        # Changing field 'Note.user'
        db.alter_column(u'api_note', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']))

        # Changing field 'Collection.user'
        db.alter_column(u'api_collection', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']))

        # Changing field 'Task.collection'
        db.alter_column(u'api_task', 'collection_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.Collection'], null=True))

        # Changing field 'Task.user'
        db.alter_column(u'api_task', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']))

        # Changing field 'Event.user'
        db.alter_column(u'api_event', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']))

    def backwards(self, orm):
        # Adding model 'User'
        db.create_table(u'api_user', (
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=20, null=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, unique=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'api', ['User'])


        # Changing field 'Note.user'
        db.alter_column(u'api_note', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.User']))

        # Changing field 'Collection.user'
        db.alter_column(u'api_collection', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.User']))

        # Changing field 'Task.collection'
        db.alter_column(u'api_task', 'collection_id', self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['api.Collection']))

        # Changing field 'Task.user'
        db.alter_column(u'api_task', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.User']))

        # Changing field 'Event.user'
        db.alter_column(u'api_event', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.User']))

    models = {
        u'api.collection': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'Collection'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'topic': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'api.event': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'Event'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'desc': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'signifiers': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['api.Signifier']", 'through': u"orm['api.EventSignifier']", 'symmetrical': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'api.eventsignifier': {
            'Meta': {'object_name': 'EventSignifier'},
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Event']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'signifier': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Signifier']"})
        },
        u'api.note': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'Note'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'signifiers': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['api.Signifier']", 'through': u"orm['api.NoteSignifier']", 'symmetrical': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'api.notesignifier': {
            'Meta': {'object_name': 'NoteSignifier'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'note': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Note']"}),
            'signifier': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Signifier']"})
        },
        u'api.signifier': {
            'Meta': {'object_name': 'Signifier'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'api.task': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'Task'},
            'collection': ('django.db.models.fields.related.ForeignKey', [], {'default': "''", 'to': u"orm['api.Collection']", 'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'desc': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'signifiers': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['api.Signifier']", 'through': u"orm['api.TaskSignifier']", 'symmetrical': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'api.tasksignifier': {
            'Meta': {'object_name': 'TaskSignifier'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'signifier': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Signifier']"}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Task']"})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['api']