# World Clock and Real-time Data Application

This Streamlit-based application offers users an intuitive interface for viewing world clocks across different time zones, converting timestamps between UNIX and human-readable formats, and accessing real-time weather data for various locations.

## Features

- **World Clock**: Displays the current time in multiple time zones selected by the user.
- **Timestamp Converter**: Converts timestamps from UNIX to human-readable format and vice versa.
- **Real-time Weather Data**: Presents the latest weather conditions for a specified city and country.

## Dependencies

- Python 3.6+
- Streamlit
- pytz
- SQLite3
- Requests (for potential future enhancements involving real-time data fetching)

## Setup

1. **Install Python**: Ensure Python 3.6 or newer is installed on your system.
2. **Clone the Repository**: Clone this repository to your local machine or directly download the `.py` file.
3. **Install Dependencies**: Execute the following command to install necessary Python packages:

   ```bash
   pip install streamlit pytz sqlite3 requests
   
Database Setup: This application requires an SQLite database (world.db) with weather_data and locations tables for storing weather data.
## Application Navigation

- The sidebar allows users to switch between World Clock, Timestamp Converter, and Real-time Data pages.
- On the World Clock page, users can select up to four time zones to view their current times.
- The Timestamp Converter page allows users to input a UNIX timestamp for conversion to a human-readable format and vice versa.
- On the Real-time Data page, users can enter a location in 'City, Country' format to fetch the latest weather data for that location.

## Contributing
We welcome contributions to this project. Please open an issue or submit a pull request with your suggestions.
Feel free to adjust the README as necessary to match your project's details and requirements.
This template outlines the basic structure and information for a README file tailored to your application. Remember to fill in any placeholders (like the license section) with the appropriate information for your project.


