from confluent_kafka import admin, Producer
import requests
import pickle
import json

city = "santiago"
api_key = "e9185b28e9969fb7a300801eb026de9c"

KAFKA_CONFIG = {
    "bootstrap.servers": "localhost:9092"
}

def current_city(id_city, api_key):
    url = "http://api.openweathermap.org/data/2.5/weather?id={}&appid={}"
    url = url.format(id_city, api_key)
    res = requests.get(url)
    data = res.json()
    return data


with open('city.list.json') as json_file:
    cities = json.load(json_file)

print(len(cities))
chile = []
for index, city in enumerate(cities):
    if city["country"] == "CL":
        chile.append(city)

print(len(chile))

calls = 0
kafka_client = admin.AdminClient(KAFKA_CONFIG)
new_topic = admin.NewTopic("weather", 1, 1)
kafka_client.create_topics([new_topic])
producer = Producer(KAFKA_CONFIG)
while True:
    for index, city in enumerate(chile):
        calls += 1
        id_city = 3868121

        query = current_city(id_city, api_key)
        if query["cod"] != 200:
            print(f"Error in {city['name']}")
            break
        else:
            print(f"{calls} | Query for {id_city} 	{query['main']}")
            producer.produce("weather", pickle.dumps(query))
