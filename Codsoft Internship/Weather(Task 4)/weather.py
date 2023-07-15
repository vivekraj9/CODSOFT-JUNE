import requests
import tkinter as tk
from tkinter import messagebox

def get_weather(city):
    # Replace 'YOUR_API_KEY' with your OpenWeatherMap API key
    api_key = '6ff818359beee1b1377bafed8148417c'
    base_url = 'http://api.openweathermap.org/data/2.5/weather'

    # Send a GET request to OpenWeatherMap API
    response = requests.get(base_url, params={'q': city, 'appid': api_key, 'units': 'metric'})

    # Process the response
    if response.status_code == 200:
        weather_data = response.json()

        # Extract relevant information from the response
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        description = weather_data['weather'][0]['description']

        # Display weather information in a message box
        messagebox.showinfo("Weather Information", f"Weather in {city}:\n\nTemperature: {temperature}°C\nHumidity: {humidity}%\nDescription: {description}")
    else:
        messagebox.showerror("Error", f"Error retrieving weather information for {city}. Error code: {response.status_code}")

# Create the main window
window = tk.Tk()
window.title("Weather Checker")
window.geometry("400x200")  # Set the window size

# Create a label
label = tk.Label(window, text="Enter a city name:", font=("Arial", 16))
label.pack(pady=10)

# Create an entry field
entry = tk.Entry(window, font=("Arial", 14))
entry.pack(pady=10)

def check_weather():
    city = entry.get()
    get_weather(city)

# Create a button to check the weather
button = tk.Button(window, text="Check Weather", command=check_weather, font=("Arial", 14), bg="light blue")
button.pack(pady=10)

# Start the main loop
window.mainloop()
