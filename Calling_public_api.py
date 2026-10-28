
import requests

API_KEY = "c8866269ed2169a9596165e04ff37be1"
CITY = "Bengaluru"
URL = "https://api.openweathermap.org/data/2.5/weather"

params = {
"q": CITY,
"appid": API_KEY,
"units": "metric"
}

try: 
  response = requests.get(URL, params=params, timeout=10)
  response.raise_for_status()
  data = response.json()
  #print(data)

  # Extract the required details
  temperature = data["main"]["temp"]
  description = data["weather"][0]["description"]
  humidity = data["main"]["humidity"]

  # Print the results
  print("City:", data["name"])
  print("Temperature:", temperature, "°C")
  print("Weather Description:", description)
  print("Humidity:", humidity, "%")

except requests.exceptions.HTTPError as e:
  print("HTTP Error:", e)
  print("Response:", response.text)

except requests.exceptions.RequestException as e:
  print("Request Error:", e)

except (KeyError, IndexError) as e:
  print("Error extracting weather data:", e)  

except Exception as e:
  print("Exception occurrred", e)

else:
  print("Weather data extraction done for City", data["name"]) 

finally:
  print("Reading Data for openweathermap done")


