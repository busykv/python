'''
go on https://www.weather-forecast.com/
make an account and get an API and copy paste your API in line 10
'''
import pyowm

city = input('enter city name: ')
country = input('enter country name: ')
owm = pyowm.OWM('COPY PASTE YOUR API HERE')
observation = owm.weather_at_place(f"{city},{country}")
w = observation.get_weather()
temperature = w.get_temperature('celsius')
refrence_time = w.get_reference_time('iso')
wind = w.get_wind('miles_hour')
sunset = w.get_sunset_time('iso')
sunrise = w.get_sunrise_time('iso')
clouds = w.get_clouds()
humidity = w.get_humidity()
pressure = w.get_pressure()
status = w.get_status()
visibility = w.get_visibility_distance()



print(f'temperature will be {temperature}')
print(f'weather was measured at {refrence_time}')
print(f'wind will be {wind} in miles_per_hour')
print(f'sunrisen at {sunrise} and sunset will be at {sunset}')
print(f'there will be {clouds}% cloudy')
print(f'humidity will be {humidity}%')
print(f'pressure will be {pressure}')
print(f'In short there will be {status}')
print(f'visibility will be {visibility}')