from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from twilio.rest import TwilioRestClient
from findmycarapp.models import Device, LocationSMS
import datetime
import logging
import sys
from urllib.parse import urlparse, parse_qs
import re
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
log = logging.getLogger(__name__)

def index(request):
	return HttpResponse("Hello World! You're at the index page.")


def send_sms(sms_to, sms_body):
	sms_from = "+17818503507"
	ACCOUNT_SID = "AC2b9daf9a366930d914fa56be530a5f0e"
	AUTH_TOKEN = "434bd7072378dd99ab63892c04182f94"

	client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
	message = client.messages.create(to=sms_to, from_=sms_from, body=sms_body)

	return


def send_request_sms_to_device(device_id):
	#Get phone number of device sim card
	device = Device.objects.get(device_id=device_id)
	send_sms(device.device_phone_no, "This is FindMyCar App. Reply back with location.")

@csrf_exempt
def receive_sms(request):
	sms_from = sms_to = sms_body = gps_lat = gps_long = None
	l = []
	try:
		sms_body = request.POST['Body']
		maps_url = re.search("(?P<url>https?://[^\s]+)", sms_body).group("url")
		parsed_url = urlparse(maps_url)
		qs = parse_qs(parsed_url.query)
		list_coord = qs['q'][0].split(",") #[<lat>, <long>]
		gps_lat = list_coord[0]
		gps_long = list_coord[1]
	except:
		msg = "Unexpected error: " + str(sys.exc_info()[0])
		log.error(msg)
		raise
	try:
		sms_from = request.POST['From']
	except:
		msg = "Unexpected error: " + str(sys.exc_info()[0])
		log.error(msg)
		raise
	try:
		sms_to = request.POST['To']
	except:
		msg = "Unexpected error: " + str(sys.exc_info()[0])
		log.error(msg)
		raise
	if sms_from is not None and sms_to is not None:
		sms = LocationSMS(sms_from=sms_from, sms_to=sms_to, message_sid="", sms_time=datetime.datetime.now(),
		                  sms_direction="", sms_body=sms_body, sms_cost=0.00, gps_latitude=gps_lat, gps_longitude=gps_long)
		sms.save()
		log_msg = "SMS saved. "+"From: "+sms_from+" To: "+sms_to+" <body>"+sms_body+"</body>"
		log.debug(log_msg)
	return render_to_response('receive_sms.html', {'sms_body': sms_body, 'sms_from': sms_from, 'sms_to': sms_to},
	                          context_instance=RequestContext(request))
