from django.http import HttpResponse
from django.shortcuts import render
from pip._vendor import requests

# Create your views here.
def home(request):
    newurl = "https://api.thingspeak.com/channels/1360342/fields/1.json?api_key=N8YVC3T7J9UJFPNV&results=1"
    print(newurl)
    get_data = requests.get(newurl).json()
    k = (get_data['feeds'])
    print(k)
    g = (k[0]['field1'])
    n = k[0]['created_at']
    return render(request, 'home.html', {'field': g, 'created': n})
