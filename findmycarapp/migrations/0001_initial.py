# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Device'
        db.create_table('findmycarapp_device', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('device_id', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('device_phone_no', self.gf('django.db.models.fields.CharField')(blank=True, max_length=30)),
            ('device_manufacturer', self.gf('django.db.models.fields.CharField')(blank=True, max_length=200)),
            ('device_model_no', self.gf('django.db.models.fields.CharField')(blank=True, max_length=200)),
        ))
        db.send_create_signal('findmycarapp', ['Device'])

        # Adding model 'LocationSMS'
        db.create_table('findmycarapp_locationsms', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sms_from', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('sms_to', self.gf('django.db.models.fields.CharField')(blank=True, max_length=30)),
            ('message_sid', self.gf('django.db.models.fields.CharField')(blank=True, max_length=60)),
            ('sms_time', self.gf('django.db.models.fields.DateTimeField')(blank=True, null=True)),
            ('sms_direction', self.gf('django.db.models.fields.CharField')(blank=True, max_length=30)),
            ('sms_status', self.gf('django.db.models.fields.CharField')(blank=True, max_length=30)),
            ('sms_body', self.gf('django.db.models.fields.CharField')(blank=True, max_length=200)),
            ('sms_cost', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=2, null=True, blank=True)),
            ('gps_latitude', self.gf('django.db.models.fields.FloatField')()),
            ('gps_longitude', self.gf('django.db.models.fields.FloatField')()),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now_add=True)),
        ))
        db.send_create_signal('findmycarapp', ['LocationSMS'])


    def backwards(self, orm):
        # Deleting model 'Device'
        db.delete_table('findmycarapp_device')

        # Deleting model 'LocationSMS'
        db.delete_table('findmycarapp_locationsms')


    models = {
        'findmycarapp.device': {
            'Meta': {'object_name': 'Device'},
            'device_id': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'device_manufacturer': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '200'}),
            'device_model_no': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '200'}),
            'device_phone_no': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'findmycarapp.locationsms': {
            'Meta': {'object_name': 'LocationSMS'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'gps_latitude': ('django.db.models.fields.FloatField', [], {}),
            'gps_longitude': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message_sid': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '60'}),
            'sms_body': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '200'}),
            'sms_cost': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '2', 'null': 'True', 'blank': 'True'}),
            'sms_direction': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'sms_from': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'sms_status': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'sms_time': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'null': 'True'}),
            'sms_to': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'})
        }
    }

    complete_apps = ['findmycarapp']