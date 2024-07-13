from django.shortcuts import render,redirect
import requests
from django.contrib import messages
from decouple import config





def get_weather_data(city_name):
    API_key=config("API_key")
    url=f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}'
    response=requests.get(url)
    if response.status_code==200:
        data=response.json()
        
        return data
        
      

    else:
        print(response.status_code)
        return None





def index(request):
    if request.method=='POST':
        city=request.POST.get('city')
        weather_data=get_weather_data(city)
        print(weather_data)
        if weather_data is not None:
           
            icon=weather_data['weather'][0]['icon']
            description=weather_data['weather'][0]['description']
            temperature=round(weather_data['main']['temp']-273.15)
            city_name=weather_data['name']
            country=weather_data['sys']['country']

            context={
                'icon':icon,
                'description':description,
                'temperature':temperature,
                'city':city_name,
                'country':country
            }
            return render(request,'index.html',context)
        
        else:
            messages.error(request,"The city you have searched is invalid")
            return redirect('/')

   
    return render(request,'index.html')