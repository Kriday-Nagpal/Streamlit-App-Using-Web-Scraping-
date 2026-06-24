import requests
import streamlit as st

st.title("🌤 Weather Scraper App")

city = st.text_input("Enter City", "London")

if st.button("Get Weather"):

    url = f"https://wttr.in/{city}?format=j1"

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        current = data["current_condition"][0]

        temp = current["temp_C"]
        humidity = current["humidity"]
        wind = current["windspeedKmph"]
        condition = current["weatherDesc"][0]["value"]

        st.subheader(f"Weather in {city}")

        st.write(f"🌡 Temperature: {temp} °C")
        st.write(f"☁ Condition: {condition}")
        st.write(f"💧 Humidity: {humidity}%")
        st.write(f"💨 Wind Speed: {wind} km/h")

    else:
        st.error("Failed to fetch weather data.")
