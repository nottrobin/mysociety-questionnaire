# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        """
            Import all political parties from the the Guardian API

        """

        from questionnaire.apihelpers import json_response

        response_data = json_response('http://www.theguardian.com/politics/api/party/all/json')
        parties_data = response_data['parties']

        for party_data in parties_data:
            party = orm.Party(name=party_data['name'], abbreviation=party_data['abbreviation'])
            party.save()

    def backwards(self, orm):
        """ Empty the party table """

        orm.Party.objects.all().delete()

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
    symmetrical = True
