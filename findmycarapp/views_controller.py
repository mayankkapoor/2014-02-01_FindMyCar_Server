from django.http import HttpResponse
from twilio.rest import TwilioRestClient

# Create your views here.
def index(request):
	return HttpResponse("Hello World! You're at the index page.")

def send_SMS(request):
	sms_to = request.GET['sms_to']
	sms_body = request.GET['sms_body']
	sms_from = "+17818503507"
	ACCOUNT_SID = "AC2b9daf9a366930d914fa56be530a5f0e"
	AUTH_TOKEN = "434bd7072378dd99ab63892c04182f94"

	client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
	message = client.messages.create(to=sms_to, from_=sms_from, body=sms_body)

	return HttpResponse("SMS sent. Check phone.")

