# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table(u'api_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=20, null=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=75)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'api', ['User'])

        # Adding model 'Signifier'
        db.create_table(u'api_signifier', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'api', ['Signifier'])

        # Adding model 'Note'
        db.create_table(u'api_note', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'api', ['Note'])

        # Adding model 'Event'
        db.create_table(u'api_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('desc', self.gf('django.db.models.fields.CharField')(max_length=250, null=True)),
        ))
        db.send_create_signal(u'api', ['Event'])

        # Adding model 'Collection'
        db.create_table(u'api_collection', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.User'])),
            ('topic', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'api', ['Collection'])

        # Adding model 'Task'
        db.create_table(u'api_task', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.User'])),
            ('collection', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.Collection'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('desc', self.gf('django.db.models.fields.CharField')(max_length=250, null=True)),
        ))
        db.send_create_signal(u'api', ['Task'])

        # Adding model 'EventSignifier'
        db.create_table(u'api_eventsignifier', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.Event'])),
            ('signifier', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.Signifier'])),
        ))
        db.send_create_signal(u'api', ['EventSignifier'])

        # Adding model 'NoteSignifier'
        db.create_table(u'api_notesignifier', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('note', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.Note'])),
            ('signifier', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.Signifier'])),
        ))
        db.send_create_signal(u'api', ['NoteSignifier'])

        # Adding model 'TaskSignifier'
        db.create_table(u'api_tasksignifier', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('task', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.Task'])),
            ('signifier', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.Signifier'])),
        ))
        db.send_create_signal(u'api', ['TaskSignifier'])


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table(u'api_user')

        # Deleting model 'Signifier'
        db.delete_table(u'api_signifier')

        # Deleting model 'Note'
        db.delete_table(u'api_note')

        # Deleting model 'Event'
        db.delete_table(u'api_event')

        # Deleting model 'Collection'
        db.delete_table(u'api_collection')

        # Deleting model 'Task'
        db.delete_table(u'api_task')

        # Deleting model 'EventSignifier'
        db.delete_table(u'api_eventsignifier')

        # Deleting model 'NoteSignifier'
        db.delete_table(u'api_notesignifier')

        # Deleting model 'TaskSignifier'
        db.delete_table(u'api_tasksignifier')


    models = {
        u'api.collection': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'Collection'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'topic': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.User']"})
        },
        u'api.event': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'Event'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'desc': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'signifiers': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['api.Signifier']", 'through': u"orm['api.EventSignifier']", 'symmetrical': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.User']"})
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
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.User']"})
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
            'collection': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Collection']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'desc': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'signifiers': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['api.Signifier']", 'through': u"orm['api.TaskSignifier']", 'symmetrical': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.User']"})
        },
        u'api.tasksignifier': {
            'Meta': {'object_name': 'TaskSignifier'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'signifier': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Signifier']"}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Task']"})
        },
        u'api.user': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'User'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['api']