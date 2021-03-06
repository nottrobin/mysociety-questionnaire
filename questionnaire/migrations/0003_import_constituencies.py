# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        """
            Import all constutuencies from the mySociety API

        """

        from questionnaire.apihelpers import json_response

        api_key = 'BaNG5WFpYN2nDnnULMAW2bGV'
        encoding = 'latin1'
        constituencies_data = json_response('http://www.theyworkforyou.com/api/getConstituencies?key=' + api_key, encoding)

        for constituency_data in constituencies_data:
            constituency = orm.Constituency(name=constituency_data['name'])
            constituency.save()

    def backwards(self, orm):
        """ Empty the constituency table """

        orm.Constituency.objects.all().delete()

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
