# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
import random
import requests

# Weather API
url = "https://weatherapi-com.p.rapidapi.com/forecast.json"

querystring = {"q":"94044", "days":"1"}

headers = {
	"X-RapidAPI-Key": "4a8352a00dmsh1bf9079140aeeb7p1439c3jsnd4531e0c0efa",
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
	"X-RapidAPI-Key": "4a8352a00dmsh1bf9079140aeeb7p1439c3jsnd4531e0c0efa",
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
# test = "Good morning, " + user_name + "!\n\n" + "Here is your joke of the day: " + "FILLER\n\n" + "The weather today is: " + "FILLER\n\n" + "Have a wonderful day." 
test = "Good morning!\n\n" + "The temperature today for " + city + " is a HIGH of " + str(high_tempF) + " and a LOW of " + str(low_tempF) + ".\nSUNSET is at " + str(sunset) + ".\n\n" + "Joke of the day:\n" + setup + "\n" + punchline + "\n\nHave a wonderful day." 
message = client.messages \
                .create(
                     messaging_service_sid='MG5b064236b195a720221403b7913f6be4',
                     body=test,
                     to='+16505156902'
                 )

# print(message.sid)

