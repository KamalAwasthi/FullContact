import requests

def getContacts(email):
	payload = {'email': email}
	r = requests.get('https://api.fullcontact.com/v2/person.json', params=payload, headers={"X-FullContact-APIKey": "95fbaf9456bfb67b"})
	print r.status_code
	return r.text