from django.shortcuts import render
import json
import urllib.request

# Create your views here.


def weather(request):
    if request.method == 'POST':
        city = request.POST['search']
        if city.strip() != '':
            res = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q=' +
                                        city+'&appid=a2b7fe9b2c19e448225b4b88c59cfa1d').read()
            json_data = json.loads(res)
            data = {
                "country_code": str(json_data['sys']['country']),
                "coordinate": str(json_data['coord']['lon']),
                "temp": str(json_data['main']['temp']) + 'k',
                "pressure": str(json_data['main']['pressure']),
                "humidity": str(json_data['main']['humidity']),
            }
        else:
            data = {}
            city = ""
    else:
        data = {}
        city = ""
    return render(request, 'weather.html', {"data": data, "city": city})
