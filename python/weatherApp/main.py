import tkinter as tk                    # GUI module for creating window applications
import requests                         # To send HTTP requests to API
from config import MY_API_KEY           # Your API key file

# Base address for downloading weather forecast from OpenWeatherMap
BASE_URL = "http://api.openweathermap.org/data/2.5/forecast?id=524901&appid="

# Initialize the main application window
window = tk.Tk()
window.geometry("800x400")
window.title("Weather App")
window.config(bg='white')

# Function to convert temperature from Kelvin to Celsius and Fahrenheit
def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return celsius, fahrenheit

# Main function responsible for weather search
def searchWeather():
    try:
        CITY = searchInput.get()                        # Getting city name from text field
        url = BASE_URL + MY_API_KEY + "&q=" + CITY      # Building the query URL
        response = requests.get(url).json()             # Sending the request and converting the response to JSON

        # Reading weather data from API response
        temp_kelvin = response['list'][0]['main']['temp']
        temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)
        feels_like_kelvin = response['list'][0]['main']['feels_like']
        feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_fahrenheit(feels_like_kelvin)
        wind_speed = response['list'][0]['wind']['speed']
        humidity = response['list'][0]['main']['humidity']
        description = response['list'][1]["weather"][0]['description']

        # Formatting results as readable text
        result = result = (
            f"📍 Weather in {CITY}\n\n"
            f"🌡️ Temperature: {temp_celsius:.2f}°C / {temp_fahrenheit:.2f}°F\n"
            f"🤔 Feels like: {feels_like_celsius:.2f}°C / {feels_like_fahrenheit:.2f}°F\n"
            f"💧 Humidity: {humidity}%\n"
            f"💨 Wind speed: {wind_speed} m/s\n"
            f"🌥️ Condition: {description.capitalize()}"
        )

        # Insert the result into the text field
        resultBox.config(state=tk.NORMAL) 
        resultBox.delete('1.0', tk.END)
        resultBox.insert('1.0', result, "center")
        resultBox.config(state=tk.DISABLED)
    
    except Exception:
        # Error handling (e.g. no city or no connection)
        resultBox.config(state=tk.NORMAL)
        resultBox.delete("1.0", tk.END)
        resultBox.insert("1.0", "No results found.", "center")
        resultBox.config(state=tk.DISABLED)



# ---------------- UI ELEMENTS ----------------#

header = tk.Label(window, text="Weather App", font=("Arial", 20), bg='white')
header.pack(pady=10)

searchInput = tk.Entry(window, width=50, borderwidth=5)
searchInput.pack(pady=10)

searchBtn = tk.Button(window, text="Search", command=searchWeather)
searchBtn.pack()

resultBox = tk.Text(window, 
              width=1000, 
              height=300,
              border=0,
              font=('Arial', 12),
              relief="flat")
resultBox.tag_config("center", justify="center")
resultBox.config(state=tk.DISABLED)
resultBox.pack(padx=10, pady=10)

# Uruchomienie pętli głównej aplikacji
window.mainloop()
