# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'AnswerSet.voting_for'
        db.alter_column(u'questionnaire_answerset', 'voting_for_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['questionnaire.Party'], null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'AnswerSet.voting_for'
        raise RuntimeError("Cannot reverse this migration. 'AnswerSet.voting_for' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'AnswerSet.voting_for'
        db.alter_column(u'questionnaire_answerset', 'voting_for_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['questionnaire.Party']))

    models = {
        u'questionnaire.answerset': {
            'Meta': {'object_name': 'AnswerSet'},
            'constituency': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['questionnaire.Constituency']"}),
            'going_to_vote': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'voting_for': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['questionnaire.Party']", 'null': 'True'})
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