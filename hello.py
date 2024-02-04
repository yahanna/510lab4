import schedule
import time
from data import fetch_and_store_weather_data  # 确保这个函数在这个文件里或者正确地从其他地方导入

api_key = "d1bdfd06881bbff02296606bc8a6ce9b"  # 你的API密钥
cities = [("London", "UK"), ("Paris", "France"), ("Berlin", "Germany")]  # 举例，你可以根据需要更新

def scheduled_job():
    for city_name, country in cities:
        fetch_and_store_weather_data(api_key, city_name, country)
        print(f"Data fetched for {city_name}, {country}")

schedule.every(30).minutes.do(scheduled_job)
# 运行定时任务
while True:
    schedule.run_pending()
    time.sleep(1)