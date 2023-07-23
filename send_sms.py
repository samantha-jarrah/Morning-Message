# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
import requests
from datetime import datetime

# Weather API
url = "https://weatherapi-com.p.rapidapi.com/forecast.json"

querystring = {"q":"94044", "days":"1"}

headers = {
    "X-RapidAPI-Key": os.environ['WEATHER_API_KEY'],
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

# Weather data points
city = response.json()['location']['name']
high_tempF = response.json()['forecast']['forecastday'][0]['day']['maxtemp_f']
low_tempF= response.json()['forecast']['forecastday'][0]['day']['mintemp_f']
sunset = response.json()['forecast']['forecastday'][0]['astro']['sunset']

# print(response.json())

# Joke API
url = "https://dad-jokes.p.rapidapi.com/random/joke"

headers = {
	"X-RapidAPI-Key": os.environ['JOKE_API_KEY'],
	"X-RapidAPI-Host": "dad-jokes.p.rapidapi.com"
}

response = requests.get(url, headers=headers)
setup = response.json()['body'][0]['setup']
punchline = response.json()['body'][0]['punchline']

# print(response.json())

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

# user_name = input("What is your name?: ")
text = "Good morning!\n\n" + "The temperature today for " + city + ":\n" + "HIGH of " + str(high_tempF) + "F\n" + "LOW of " + str(low_tempF) + "F\nSUNSET is at " + str(sunset) + "\n\n" + "Joke of the day:\n" + setup + "\n" + punchline + "\n\nHave a wonderful day." 
message = client.messages \
                .create(
                     messaging_service_sid='MG5b064236b195a720221403b7913f6be4',
                     body=text,
                    #  send_at=datetime(2023, 7, 11, 2, 37, 1),
                    #  schedule_type='fixed',
                     to='+16505156902'
                 )

print(message.sid)

