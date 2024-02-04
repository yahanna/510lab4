
import sqlite3
conn = sqlite3.connect('world.db')
import requests


cursor = conn.cursor()

    # 创建weather_data表
create_weather_data_table_query = """
    CREATE TABLE IF NOT EXISTS weather_data (
        weather_id INTEGER PRIMARY KEY AUTOINCREMENT,
        location_id INTEGER,
        temperature REAL,
        humidity INTEGER,
        weather_description TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(location_id) REFERENCES locations(location_id)
    );
    """
cursor.execute(create_weather_data_table_query)

    # 创建emergency_calls表
create_emergency_calls_table_query = """
    CREATE TABLE IF NOT EXISTS emergency_calls (
        call_id INTEGER PRIMARY KEY AUTOINCREMENT,
        location_id INTEGER,
        call_type TEXT,
        description TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(location_id) REFERENCES locations(location_id)
    );
    """
cursor.execute(create_emergency_calls_table_query)

conn.commit()
conn.close()



def fetch_and_store_weather_data(api_key, city_name, country):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name},{country}&appid={api_key}&units=metric"

    response = requests.get(url)
    if response.status_code == 200:
        weather_data = response.json()

        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        weather_description = weather_data["weather"][0]["description"]

        conn = sqlite3.connect('world.db')
        cursor = conn.cursor()

        # 确保先有对应的location数据
        cursor.execute("INSERT OR IGNORE INTO locations (city_name, country) VALUES (?, ?)", (city_name, country))
        conn.commit()

        # 获取location_id
        cursor.execute("SELECT location_id FROM locations WHERE city_name = ? AND country = ?", (city_name, country))
        location_id = cursor.fetchone()[0]

        insert_query = """
            INSERT INTO weather_data (location_id, temperature, humidity, weather_description)
            VALUES (?, ?, ?, ?);
        """
        cursor.execute(insert_query, (location_id, temperature, humidity, weather_description))
        
        conn.commit()
        conn.close()
    else:
        print(f"Error fetching weather data: Status code {response.status_code}")

def get_latest_weather_data(city_name, country):
    conn = sqlite3.connect('world.db')
    cursor = conn.cursor()

    query = """
    SELECT temperature, humidity, weather_description, timestamp
    FROM weather_data
    JOIN locations ON weather_data.location_id = locations.location_id
    WHERE city_name = ? AND country = ? 
    ORDER BY timestamp DESC
    LIMIT 1;
    """
    cursor.execute(query, (city_name, country))
    data = cursor.fetchone()  # fetchone()可能返回None，如果查询结果为空

    conn.close()

    if data:
        return data
    else:
        # 如果没有找到数据，可以返回None或者一个表示没有数据的消息
        return None
