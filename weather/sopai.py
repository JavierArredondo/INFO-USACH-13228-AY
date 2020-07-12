from confluent_kafka import admin, Producer
import requests
import logging
import pickle
import json
import os

WORKING_DIRECTORY = os.path.dirname(os.path.abspath(__file__))

city = "santiago"
api_key = "e9185b28e9969fb7a300801eb026de9c"

KAFKA_CONFIG = {
    "bootstrap.servers": "localhost:9092"
}

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(name)s.%(funcName)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


def current_city(id_city, api_key):
    url = "http://api.openweathermap.org/data/2.5/weather?id={}&appid={}"
    url = url.format(id_city, api_key)
    res = requests.get(url)
    data = res.json()
    return data


with open(os.path.join(WORKING_DIRECTORY, 'city.list.json')) as json_file:
    cities = json.load(json_file)

chile = []
for index, city in enumerate(cities):
    if city["country"] == "CL":
        chile.append(city)

logging.info(f"Total cities {len(chile)}")

calls = 0
kafka_client = admin.AdminClient(KAFKA_CONFIG)
new_topic = admin.NewTopic("weather", 1, 1)
kafka_client.create_topics([new_topic])
producer = Producer(KAFKA_CONFIG)
while True:
    for index, city in enumerate(chile):
        calls += 1

        query = current_city(city['id'], api_key)
        if query["cod"] != 200:
            logging.error(f"Error in {index} {city}")
            break
        else:
            logging.info(f"calls: {calls} city: {city['name']}")
            producer.produce("weather", pickle.dumps(query))
