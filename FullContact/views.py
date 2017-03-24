from django.shortcuts import render
from django.http import HttpResponse
from .forms import GetEmail
from .utils import * 
import json


# Create your views here.

def getFullContact(request):
    if request.method == 'POST':
        email = GetEmail(request.POST)
        r = getContacts(email['email'].value())
        response = json.loads(r)
        responseStatus = response['status']
        try:
        	photos = response['photos']
        except Exception as e:
        	photos = ''

    	try:
    		contactInfo = response['contactInfo']
    	except Exception as e:
    		contactInfo = ''

    	try:
    		socialProfiles = response['socialProfiles']
    	except Exception as e:
    		socialProfiles = ''


    	if(responseStatus == 200):
    		if(photos == '' and contactInfo == '' and socialProfiles == ''):
    			message = "Nothing found for the given email address!!"
    		else:
    			message = ''
    		return render(request,'FullContacts/getEmail.html',{'form':email,'status_code': responseStatus,
    		'id':response['requestId'], 'text':r, 'photos':photos, 'contactInfo':contactInfo, 
    		'socialProfiles':socialProfiles,'msg':message})

    	if(responseStatus == 202):
    		return HttpResponse("Your Query has been recorded. It is queued for search, please check again after some time.")
    	else:
    		return render(request,'FullContacts/oops.html',{'msg':response['message']})

    else:
    	email = GetEmail()
    return render(request,'FullContacts/getEmail.html',{'form':email})
