import requests
import bs4 

apikey="a2480c334932e8c295d190afc9d32046"
baseURL="https://api.openweathermap.org/data/2.5/weather?=q"
cityName= input("Enter your City: ")
completeURL=baseURL+cityName+"&appid="+apikey 

response=requests.get(completeURL)
data=response.json()
print(data)
