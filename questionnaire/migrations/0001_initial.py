# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Constituency'
        db.create_table(u'questionnaire_constituency', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'questionnaire', ['Constituency'])

        # Adding model 'Party'
        db.create_table(u'questionnaire_party', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('abbreviation', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'questionnaire', ['Party'])

        # Adding model 'AnswerSet'
        db.create_table(u'questionnaire_answerset', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('constituency', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['questionnaire.Constituency'])),
            ('going_to_vote', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('voting_for', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['questionnaire.Party'])),
        ))
        db.send_create_signal(u'questionnaire', ['AnswerSet'])


    def backwards(self, orm):
        # Deleting model 'Constituency'
        db.delete_table(u'questionnaire_constituency')

        # Deleting model 'Party'
        db.delete_table(u'questionnaire_party')

        # Deleting model 'AnswerSet'
        db.delete_table(u'questionnaire_answerset')


    models = {
        u'questionnaire.answerset': {
            'Meta': {'object_name': 'AnswerSet'},
            'constituency': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['questionnaire.Constituency']"}),
            'going_to_vote': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'voting_for': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['questionnaire.Party']"})
        },
        u'questionnaire.constituency': {
            'Meta': {'object_name': 'Constituency'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'questionnaire.party': {
            'Meta': {'object_name': 'Party'},
            'abbreviation': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['questionnaire']