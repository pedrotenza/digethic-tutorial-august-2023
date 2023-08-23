

import requests

# Set the coordinates for Göttingen
Latitude: 51.5333
Longitude: 9.9357

## Aufgabe 1.2

# Construct the URL for the API request
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m"

# Send the GET request to the API
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Print the response code and the JSON data
    print("Response code:", response.status_code)
    print("Response JSON:", data)

    # Extract and print the temperature data
    if "hourly" in data and "temperature_2m" in data["hourly"]:
        temperature_data = data["hourly"]["temperature_2m"]
        print("Temperature data:", temperature_data)
    else:
        print("Temperature data not found in the response.")
else:
    print("Request was not successful. Status code:", response.status_code)


## Augabe 1.

