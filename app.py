import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Weather App")

st.title("Weather Scraper App")

city = st.text_input("Enter City", "London")

if st.button("Get Weather"):

    url = f"https://wttr.in/{city}"

    response = requests.get(url)

    if response.status_code == 200:

        soup = bs(response.text, "html.parser")

        weather_data = [{
            "City": city,
            "Status": "Weather data fetched successfully"
        }]

        weather_df = pd.DataFrame(weather_data)

        st.subheader("Weather Information")
        st.dataframe(weather_df)

        st.text(response.text[:1000])  # Shows first part of weather report

    else:
        st.error("Could not fetch weather data.")
