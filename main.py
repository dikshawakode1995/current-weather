import requests
add="http://api.openweathermap.org/data/2.5/weather?appid=c61442f0dde000dd2009503c09355532&q="
city=input("enter city name: ")
url=add+city
data =requests.get(url).json()
format_d=data['main']['temp']
print(format_d)
