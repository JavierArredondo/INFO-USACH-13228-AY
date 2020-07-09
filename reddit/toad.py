from confluent_kafka import admin, Producer
from sseclient import SSEClient
import ujson as json
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(name)s.%(funcName)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

STREAM_PATH = "http://stream.pushshift.io/?type=submissions"
KAFKA_CONFIG = {
    "bootstrap.servers": "localhost:9092"
}


def process_message(msg, topic, producer):
    logging.info(f"event: {msg.event} id: {msg.id}")
    data = msg.data
    json_data = json.loads(data)
    producer.produce(topic, str(json_data))


if __name__ == "__main__":
    kafka_client = admin.AdminClient(KAFKA_CONFIG)
    queue = SSEClient(STREAM_PATH)
    new_topic = admin.NewTopic("reddit", 1, 1)
    kafka_client.create_topics([new_topic])
    producer = Producer(KAFKA_CONFIG)
    for msg in queue:
        try:
            process_message(msg, "reddit", producer)
        except Exception as e:
            print(e)