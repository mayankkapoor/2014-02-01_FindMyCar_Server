from django.db import models

# Create your models here.
class Device(models.Model):
	device_id = models.CharField(max_length=200, blank=False) #unique device id
	device_phone_no = models.CharField(max_length=30, blank=True) #sim installed in device
	device_manufacturer = models.CharField(max_length=200, blank=True)
	device_model_no = models.CharField(max_length=200, blank=True) #different devices can have different sms formats

	def __str__(self):
		return u'id: %s, device_phone_no: %s' % (self.device_id, self.device_phone_no)

class LocationSMS(models.Model):
	sms_from = models.CharField(max_length=30, blank=False)
	sms_to = models.CharField(max_length=30, blank=True)
	message_sid = models.CharField(max_length=60, blank=True)
	sms_time = models.DateTimeField(blank=True, null=True)
	sms_direction = models.CharField(max_length=30, blank=True)
	sms_status = models.CharField(max_length=30, blank=True)
	sms_body = models.CharField(max_length=200, blank=True)
	sms_cost = models.DecimalField(max_digits=4,decimal_places=2, blank=True, null=True)
	gps_latitude = models.FloatField(null=False)
	gps_longitude = models.FloatField(null=False)
	created_on = models.DateTimeField(auto_now_add=True, editable=False)

	def __str__(self):
		return u'sms_from: %s, lat: %s, long: %s' % (self.sms_from, self.gps_latitude, self.gps_longitude)

