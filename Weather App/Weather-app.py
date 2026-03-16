import requests

# API key here
api_key = "e2a99a1828d673460a083e6e752609a3"

# Ask user for city
city = input("Enter city name: ")

# Weather API URL
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

# Send request
response = requests.get(url)

# Convert response to JSON
data = response.json()

# Print full API response (for debugging)
# print(data)

# Check if API returned success
if response.status_code == 200:

    if "main" in data:

        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather = data["weather"][0]["description"]

        print("\nWeather Details")
        print("City:", city)
        print("Temperature:", temperature, "°C")
        print("Humidity:", humidity)
        print("Condition:", weather)

    else:
        print("Weather data not found")

else:
    print("Error:", data["message"])
