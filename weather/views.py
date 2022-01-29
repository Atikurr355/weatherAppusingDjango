from django.shortcuts import render
import json
import urllib.request

# Create your views here.
def index(request):
    if request.method == "POST":
        city = request.POST['city']
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+"&appid=40eeb8226126042238bf8949b635d2d1").read()
        jeson_data = json.loads(res)
        data = {
            'country_code':str(jeson_data['sys']['country']),
            'coordinate':str(jeson_data['coord']['lon']) + '' +str(jeson_data['coord']['lat']),
            'temp':str(jeson_data['main']['temp'])+'k',
            'pressure':str(jeson_data['main']['pressure']),
            'humidity':str(jeson_data['main']['humidity']),
        }
    else:
        city=''
        data=''
    
    context = {
        'data':data,
        'city':city
        }

    return render(request, 'index.html',context)