from django.shortcuts import render,redirect
import requests
from django.contrib import messages
from decouple import config

API_key=config("API_key")




def get_weather_data(city_name):
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
                'country':country,
                'api_key':API_key

            }
            return render(request,'index.html',context)
        
        else:
            messages.error(request,"The city you have searched is invalid")
            return redirect('index')

   
    return render(request,'index.html',{'api_key':API_key})