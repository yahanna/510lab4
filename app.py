
import streamlit as st
import pytz
from datetime import datetime
import time
import requests
import sqlite3


# List of time zones
time_zones = list(pytz.all_timezones)

# 设置侧边栏来选择页面
page = st.sidebar.selectbox("Choose a page", ["World Clock", "Timestamp Converter", "Real-time Data"])

if page == "World Clock":
    st.title("World Clock App")

    # Multi-select dropdown for time zones
    selected_zones = st.multiselect("Choose up to 4 time zones", time_zones, default=["UTC"])

    # Placeholder for clocks
    clocks_container = st.empty()

    # Display clocks with UNIX timestamp
    with clocks_container.container():
        for zone in selected_zones:
            tz = pytz.timezone(zone)
            now = datetime.now(tz)
            time_now = now.strftime('%Y-%m-%d %H:%M:%S')
            unix_timestamp = int(now.timestamp())
            st.metric(label=zone, value=f"Local Time: {time_now}", delta=f"UNIX Timestamp: {unix_timestamp}")
    time.sleep(1)
    st.experimental_rerun()

if page == "Real-time Data":
    st.title("Real-time Data")

# 假设这个函数位于你的代码顶部或者作为一个独立的模块
def get_latest_weather_data(city_name, country):
    conn = sqlite3.connect('world.db')
    cursor = conn.cursor()
    
    # 获取最新的天气数据
    query = """
    SELECT temperature, humidity, weather_description, timestamp
    FROM weather_data
    JOIN locations ON weather_data.location_id = locations.location_id
    WHERE city_name = ? AND country = ? 
    ORDER BY timestamp DESC
    LIMIT 1;
    """
    cursor.execute(query, (city_name, country))
    data = cursor.fetchone()
    conn.close()
    
    return data

if page == "Real-time Data":
    st.title("Real-time Weather Data")

    # 为天气数据部分提供单独的输入界面
    st.header("Weather Data")
    city_country_input = st.text_input("Enter location as 'City, Country' (e.g., 'London, UK')")

    if st.button("Get Weather Data"):
        if ", " in city_country_input:
            city_name, country = city_country_input.split(", ", 1)
            data = get_latest_weather_data(city_name, country.strip())
            if data:
                temperature, humidity, weather_description, timestamp = data
                st.subheader(f"Weather in {city_name}, {country}:")
                st.write(f"Temperature: {temperature}°C")
                st.write(f"Humidity: {humidity}%")
                st.write(f"Description: {weather_description}")
                st.write(f"Last Updated: {timestamp}")
            else:
                st.write(f"No weather data available for {city_name}, {country}.")
        else:
            st.error("Invalid location format. Please use 'City, Country' format.")
    
elif page == "Timestamp Converter":
    st.title("Timestamp Converter")

    # Section for converting UNIX timestamp to human-readable time
    st.header("UNIX Timestamp to Human-readable Time")
    unix_input = st.number_input("Enter UNIX Timestamp", step=1, format="%d")
    if unix_input:
        human_time = datetime.fromtimestamp(unix_input).strftime('%Y-%m-%d %H:%M:%S')
        st.write(f"Human Readable Time: {human_time}")

    # Section for converting human-readable time to UNIX timestamp
    st.header("Human-readable Time to UNIX Timestamp")
    date_input = st.date_input("Choose a date")
    time_input = st.time_input("Choose time")
    # Combining date and time input for conversion
    datetime_combined = datetime.combine(date_input, time_input)
    if st.button("Convert to UNIX Timestamp"):
        unix_output = int(datetime_combined.timestamp())
        st.write(f"UNIX Timestamp: {unix_output}")