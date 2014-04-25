# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'TaskSignifier'
        db.delete_table(u'api_tasksignifier')

        # Deleting model 'EventSignifier'
        db.delete_table(u'api_eventsignifier')

        # Deleting model 'Note'
        db.delete_table(u'api_note')

        # Deleting model 'NoteSignifier'
        db.delete_table(u'api_notesignifier')

        # Deleting model 'Task'
        db.delete_table(u'api_task')

        # Deleting model 'Event'
        db.delete_table(u'api_event')

        # Adding model 'Page'
        db.create_table(u'api_page', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('page_number', self.gf('django.db.models.fields.IntegerField')(max_length=50)),
        ))
        db.send_create_signal(u'api', ['Page'])

        # Adding model 'Bullet'
        db.create_table(u'api_bullet', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('collection', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.Collection'], null=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('desc', self.gf('django.db.models.fields.CharField')(max_length=250, null=True)),
            ('done', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'api', ['Bullet'])

        # Adding model 'BulletCollection'
        db.create_table(u'api_bulletcollection', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('bullet', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.Bullet'])),
            ('collection', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.Collection'])),
        ))
        db.send_create_signal(u'api', ['BulletCollection'])

        # Adding model 'BulletSignifier'
        db.create_table(u'api_bulletsignifier', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('bullet', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.Bullet'])),
            ('signifier', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.Signifier'])),
        ))
        db.send_create_signal(u'api', ['BulletSignifier'])


    def backwards(self, orm):
        # Adding model 'TaskSignifier'
        db.create_table(u'api_tasksignifier', (
            ('task', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.Task'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('signifier', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.Signifier'])),
        ))
        db.send_create_signal(u'api', ['TaskSignifier'])

        # Adding model 'EventSignifier'
        db.create_table(u'api_eventsignifier', (
            ('signifier', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.Signifier'])),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.Event'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'api', ['EventSignifier'])

        # Adding model 'Note'
        db.create_table(u'api_note', (
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'api', ['Note'])

        # Adding model 'NoteSignifier'
        db.create_table(u'api_notesignifier', (
            ('note', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.Note'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('signifier', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.Signifier'])),
        ))
        db.send_create_signal(u'api', ['NoteSignifier'])

        # Adding model 'Task'
        db.create_table(u'api_task', (
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('collection', self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['api.Collection'], null=True)),
            ('desc', self.gf('django.db.models.fields.CharField')(max_length=250, null=True)),
        ))
        db.send_create_signal(u'api', ['Task'])

        # Adding model 'Event'
        db.create_table(u'api_event', (
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('desc', self.gf('django.db.models.fields.CharField')(max_length=250, null=True)),
        ))
        db.send_create_signal(u'api', ['Event'])

        # Deleting model 'Page'
        db.delete_table(u'api_page')

        # Deleting model 'Bullet'
        db.delete_table(u'api_bullet')

        # Deleting model 'BulletCollection'
        db.delete_table(u'api_bulletcollection')

        # Deleting model 'BulletSignifier'
        db.delete_table(u'api_bulletsignifier')


    models = {
        u'api.bullet': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'Bullet'},
            'collection': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Collection']", 'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'desc': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'}),
            'done': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'signifiers': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['api.Signifier']", 'through': u"orm['api.BulletSignifier']", 'symmetrical': 'False'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'api.bulletcollection': {
            'Meta': {'object_name': 'BulletCollection'},
            'bullet': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Bullet']"}),
            'collection': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Collection']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'api.bulletsignifier': {
            'Meta': {'object_name': 'BulletSignifier'},
            'bullet': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Bullet']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'signifier': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Signifier']"})
        },
        u'api.collection': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'Collection'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'topic': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'api.page': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'Page'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'page_number': ('django.db.models.fields.IntegerField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'api.signifier': {
            'Meta': {'object_name': 'Signifier'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
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