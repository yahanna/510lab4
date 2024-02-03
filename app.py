
import streamlit as st
import pytz
from datetime import datetime
import time

# List of time zones
time_zones = list(pytz.all_timezones)

# 设置侧边栏来选择页面
page = st.sidebar.selectbox("Choose a page", ["World Clock", "Timestamp Converter"])

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