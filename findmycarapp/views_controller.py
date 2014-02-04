from django.http import HttpResponse
from twilio.rest import TwilioRestClient
from findmycarapp.models import Device

# Create your views here.


def index(request):
	return HttpResponse("Hello World! You're at the index page.")


def send_SMS(sms_to, sms_body):
	sms_from = "+17818503507"
	ACCOUNT_SID = "AC2b9daf9a366930d914fa56be530a5f0e"
	AUTH_TOKEN = "434bd7072378dd99ab63892c04182f94"

	client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
	message = client.messages.create(to=sms_to, from_=sms_from, body=sms_body)

	return


def send_request_SMS_to_device(device_id):
	#Get phone number of device sim card
	device = Device.objects.get(device_id=device_id)
	send_SMS(device.device_phone_no, "This is FindMyCar App. Reply back with location.")