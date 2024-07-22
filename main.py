import streamlit as st
import requests
 
# Function to fetch weather details
def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "q=" + city_name + "&appid=" + api_key + "&units=metric"
    response = requests.get(complete_url)

    
   
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        wind = data['wind']
        weather_desc = data['weather'][0]['description']
        temperature = main['temp']
        humidity = main['humidity']
        wind_speed = wind['speed']
        return {
            "temperature": temperature,
            "humidity": humidity,
            "description": weather_desc,
            "wind_speed": wind_speed
        }
    else:
        return None
 
# Streamlit UI
st.title("Weather Report")
st.write("Enter the city name to get the current weather details.")
 
city_name = st.text_input("City Name")
api_key = "a2834e626f2db62b7f1a2716633d6520"  # Replace with your OpenWeatherMap API key
 
if st.button("Get Weather"):
    if city_name:
        weather = get_weather(city_name, api_key)
        if weather:
            st.success(f"Weather details for {city_name}:")
            st.write(f"**Temperature:** {weather['temperature']}°C")
            st.write(f"**Humidity:** {weather['humidity']}%")
            st.write(f"**Description:** {weather['description']}")
            st.write(f"**Wind Speed:** {weather['wind_speed']} m/s")
        else:
            st.error("City not found or unable to fetch weather details. Please try again.")
    else:
        st.error("Please enter a city name.")